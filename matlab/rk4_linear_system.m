% Classical RK4 for linear ODE system y' = Ay + b(t)
clear; clc;

A = [0 1; -1 0];
f = @(t, y) A*y + [sin(t); cos(t)];

t0 = -2.5; t1 = 10; h = 1/30;
t = t0:h:t1;
N = length(t);

y0 = [2.5*sin(2.5); -2.5*cos(2.5)];
Y = zeros(2, N);
Y(:,1) = y0;

for n = 1:N-1
    tn = t(n); yn = Y(:,n);
    k1 = f(tn, yn);
    k2 = f(tn + h/2, yn + h/2 * k1);
    k3 = f(tn + h/2, yn + h/2 * k2);
    k4 = f(tn + h,   yn + h   * k3);
    Y(:,n+1) = yn + (h/6)*(k1 + 2*k2 + 2*k3 + k4);
end

figure;
plot(t, Y(1,:), 'b-', 'LineWidth', 1.5); hold on;
plot(t, Y(2,:), 'r--', 'LineWidth', 1.5);
xlabel('t'); ylabel('y');
title('RK4 Solution of Linear ODE System');
legend('y_1(t)', 'y_2(t)');
grid on;