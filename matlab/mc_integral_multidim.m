% Monte Carlo integration for f(x) over [0,1]^d, varying d
clear; clc;

dims = 1:10;
N = 1e5;

mc_estimates = zeros(size(dims));
stddevs = zeros(size(dims));
errors = zeros(size(dims));
exact_vals = zeros(size(dims));

rng(42);

for idx = 1:length(dims)
    d = dims(idx);
    js = 1:d;
    X = rand(N, d);
    vals = prod(exp(X) ./ js, 2);
    mc_mean = mean(vals);
    std_mc = std(vals) / sqrt(N);
    exact = prod(expm1(1./js) ./ js);
    error = abs(mc_mean - exact);
    mc_estimates(idx) = mc_mean;
    stddevs(idx) = std_mc;
    errors(idx) = error;
    exact_vals(idx) = exact;
end

fprintf('%2s %13s %13s %13s %13s\n', 'd', 'MC Estimate', 'StdDev', 'Exact', 'Error');
for idx = 1:length(dims)
    fprintf('%2d %13.8f %13.8f %13.8f %13.8f\n', dims(idx), mc_estimates(idx), stddevs(idx), exact_vals(idx), errors(idx));
end

figure;
semilogy(dims, errors, 'o-', 'DisplayName','Absolute Error'); hold on;
semilogy(dims, stddevs, 's-', 'DisplayName','MC StdDev');
xlabel('Dimension d'); ylabel('Error (log scale)');
title('Monte Carlo Integration Error vs Dimension');
legend show;
grid on;