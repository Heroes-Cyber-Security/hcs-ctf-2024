FROM pwn.red/jail

COPY --from=ubuntu:22.04 / /srv
COPY flag.txt /srv/app/flag.txt
COPY flag /srv/app/run

RUN chmod 755 /srv/app/run

ENV JAIL_MEM=5M JAIL_TIME=120 JAIL_PORT=1234