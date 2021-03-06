% Strong Scaling BIDG

% Averaging:
% m* = mean(mpi_time)

% Efficiency for N threads
% e.g. e2 = (m1/(N*m2))*100

m1=mean(mpi_time1)
m2=mean(mpi_time2)
m4=mean(mpi_time4)
m8=mean(mpi_time8)
m16=mean(mpi_time16)
% m32=mean(mpi_time32)
% m64=mean(mpi_time64)
% m128=mean(mpi_time128)
% m256=mean(mpi_time256)

e1=100
e2=(m1/(2*m2))*100
e4=(m1/(4*m4))*100
e8=(m1/(8*m8))*100
e16=(m1/(16*m16))*100
% e32=(m1/(32*m32))*100
% e64=(m1/(64*m64))*100
% e128=(m1/(128*m128))*100
% e256=(m1/(256*m256))*100

c=[1 2 4 8 16 ]
e=[e1 e2 e4 e8 e16 ]

hold on
plot(log(c),e)

% lc=log(c)
% xticks(lc)
% xticklabels({'1','2','4','8','16','32','64','128','256'})
