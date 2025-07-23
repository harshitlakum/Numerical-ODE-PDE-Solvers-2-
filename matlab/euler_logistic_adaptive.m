% Explicit Euler for logistic ODE with adaptive step size
clear; clc;

f = @(t, y) (1 - y/100).*y;

t0 = 0; t1 = 10; y0 = 1;
tol = 1e-3; h = 0.1;
h_min = 1e-4; h_max = 0.5;

t_values = t0;
y_values = y0;
h_values = [];

t = t0; y = y0;

while t < t1
    if t + h > t1
        h = t1 - t;
    end
    y1 = y + h * f(t, y);
    y_half = y + (h/2) * f(t, y);
    y2 = y_half + (h/2) * f(t + h/2, y_half);
    err = abs(y2 - y1);
    if err < tol
        t = t + h;
        y = y2;
        t_values(end+1) = t;
        y_values(end+1) = y;
        h_values(end+1) = h;
        h = min(h_max, h * min(2, 0.9 * sqrt(tol/(err+1e-16))));
    else
        h = max(h_min, h * max(0.1, 0.9 * sqrt(tol/(err+1e-16))));
    end
end

figure;
subplot(1,2,1);
plot(t_values, y_values, 'b-', 'LineWidth', 1.5);
xlabel('t'); ylabel('y(t)');
title('Logistic Growth: Adaptive Euler');
grid on;

subplot(1,2,2);
plot(t_values(2:end), h_values, 'r.-', 'LineWidth', 1.5);
xlabel('t'); ylabel('Step size h');
title('Step size vs. time');
grid on;