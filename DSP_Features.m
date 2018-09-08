[S, ~, ~] = xlsread('standing.csv'); % For Standing
[R, ~, ~] = xlsread('running.csv'); % For Running
[C, ~, ~] = xlsread('cycling.csv'); % For Cycling

Sx = S(:,1); Sy = S(:,2); Sz = S(:,3);
Rx = R(:,1); Ry = R(:,2); Rz = R(:,3);
Cx = C(:,1); Cy = C(:,2); Cz = C(:,3);
f1=[];
f2=[];
f3=[];
for i = 1:270
    W1x = Sx((i*10-9):(i*10));
    W1y = Sy((i*10-9):(i*10));
    W1z = Sz((i*10-9):(i*10));
    [a, b, c, d, e, f, g, h, q, j, k, l, m, n, o ] = FeatureVec(W1x, W1y, W1z);
    f1= [f1; [a b c d e f g h q j k l m n o]];
    W2x = Rx((i*10-9):(i*10));
    W2y = Ry((i*10-9):(i*10)); 
    W2z = Rz((i*10-9):(i*10));
    [a, b, c, d, e, f, g, h, q, j, k, l, m, n, o] = FeatureVec(W2x, W2y, W2z);
    f2= [f2; [a b c d e f g h q j k l m n o]];
    W3x = Cx(i*10-9:i*10); W3y = Cy(i*10-9:i*10); W3z = Cz(i*10-9:i*10);
    [a, b, c, d, e, f, g, h, q, j, k, l, m, n, o] = FeatureVec(W3x, W3y, W3z);
    f3= [f3; [a b c d e f g h q j k l m n o]];
    
end
scatter3(f1(:,1), f1(:,2), f1(:,3), 'r');
hold on;
scatter3(f2(:,1), f2(:,2), f2(:,3), 'g');
hold on;
scatter3(f3(:,1), f3(:,2), f3(:,3), 'k');

figure
scatter3(f1(:,4), f1(:,5), f1(:,6), 'r');
hold on;
scatter3(f2(:,4), f2(:,5), f2(:,6), 'g');
hold on;
scatter3(f3(:,4), f3(:,5), f3(:,6), 'k');

figure
scatter3(f1(:,7), f1(:,8), f1(:,9), 'r');
hold on;
scatter3(f2(:,7), f2(:,8), f2(:,9), 'g');
hold on;
scatter3(f3(:,7), f3(:,8), f3(:,9), 'k');

figure
scatter3(f1(:,10), f1(:,11), f1(:,12), 'r');
hold on;
scatter3(f2(:,10), f2(:,11), f2(:,12), 'g');
hold on;
scatter3(f3(:,10), f3(:,11), f3(:,12), 'k');

figure
scatter3(f1(:,13), f1(:,14), f1(:,15), 'r');
hold on;
scatter3(f2(:,13), f2(:,14), f2(:,15), 'g');
hold on;
scatter3(f3(:,13), f3(:,14), f3(:,15), 'k');

csvwrite('fg.csv',f1);
csvwrite('fh.csv',f2);
csvwrite('fi.csv',f3);