FROM python:alpine

ENV GID=1001 \
    GNAME=group \
    UID=1001 \
    UNAME=user

# set -x: print commands and their outputs
RUN set -x && \
    apk --update add bash vim tzdata && \
    addgroup -g $GID -S $GNAME && \
    adduser -S -D -H -u $URID -h $HOME -s /sbin/nologin -G $GNAME -g $GNAME $URNAME && \
    ls -las /usr/src && \
    touch /usr/src/results && \
    chown $UID:$GID /usr/src/results && \
    #chown -R $UID:$GID /usr/src/app && \
    unlink /usr/bin/env && \
    unlink /usr/bin/top && \
    unlink /bin/ps && \
    echo user was created

# create image with right timezone for Vienna
ARG TZ=Europe/Vienna
RUN touch "/etc/timezone" && \
    ln -sf "/usr/share/zoneinfo/$TZ" /etc/localtime && \
    echo "$TZ" > /etc/timezone

WORKDIR /usr/src/app
USER $UNAME
COPY empty/ .

#ENTRYPOINT ["/bin/bash"]
#CMD ["-x","/start-mysql.sh"]

CMD ["python","./empty.py","find"]


#ENTRYPOINT ["/bin/bash"]
#CMD ["-x","/start-mysql.sh"]
