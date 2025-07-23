% Implicit midpoint vs explicit Euler for stiff ODE system
clear; clc;

s = 1000;
A = [-s, s-1; 0, -1];
y0 = [2; 1];

T = 0.01; h = 0.001;
t = 0:h:T;
N = length(t);

% Exact solution
y_exact = @(t) [exp(-s*t) + exp(-t); exp(-t)];

I = eye(2);
LHS = I - (h/2)*A;
RHS = I + (h/2)*A;
LHS_inv = inv(LHS);

y_im = zeros(2, N); y_im(:,1) = y0;
for n = 1:N-1
    y_im(:,n+1) = LHS_inv * (RHS * y_im(:,n));
end

y_ee = zeros(2, N); y_ee(:,1) = y0;
for n = 1:N-1
    y_ee(:,n+1) = y_ee(:,n) + h * (A * y_ee(:,n));
end

Y_exact = y_exact(t);

figure;
subplot(1,2,1);
plot(t, Y_exact(1,:), 'k-', 'LineWidth', 1.2); hold on;
plot(t, y_im(1,:), 'b--', 'LineWidth', 1.2);
plot(t, y_ee(1,:), 'r:', 'LineWidth', 1.2);
xlabel('t'); ylabel('y_1');
title('Component y_1');
legend('Exact', 'Implicit Midpoint', 'Explicit Euler');
grid on;

subplot(1,2,2);
plot(t, Y_exact(2,:), 'k-', 'LineWidth', 1.2); hold on;
plot(t, y_im(2,:), 'b--', 'LineWidth', 1.2);
plot(t, y_ee(2,:), 'r:', 'LineWidth', 1.2);
xlabel('t'); ylabel('y_2');
title('Component y_2');
legend('Exact', 'Implicit Midpoint', 'Explicit Euler');
grid on;