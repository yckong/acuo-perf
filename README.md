# acuo-perf

Sample command to run test:
jmeter -n -t loadDashboard.jmx -l loadDashboard.csv -J host.ip=uat.acuo.com -J host.protocol=http -J user.usercount=10 -J user.rampup=20 -J user.loopcount=1