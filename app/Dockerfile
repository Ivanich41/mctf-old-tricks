FROM ubuntu:22.04

# Installs
RUN apt-get update  \
    && apt install -y vim openssh-server socat links
RUN adduser --disabled-password --gecos "" browser

# SSH Config
RUN groupadd sshgroup && usermod -aG sshgroup browser && mkdir /var/run/sshd
RUN echo 'root:N0tRequ1r3d' | chpasswd && echo 'browser:0nlySt@rtup' | chpasswd
COPY ./sshd_config /etc/ssh/sshd_confog
RUN mkdir /home/browser/.ssh \
    && echo 'command="/usr/bin/startup.sh" ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDRwLNUVV58sYFyjmf9eqIE51m3P8qrSN+2QiwwXaDvx/qepzpfpEYnAxAG0Hh9m8pMhwn55TT4lv0u/a7LoQY5Q8Od09jX4OiiMYvfXqk2nA2Y6HJbykM76NcQAMtNFnomQi8qYpSGLWa3+hGx8QuShX/48IZg+pam6W3lFlwB9yzJhr1uT5pIKyrD4HBE5eyyl/F+d+owS5Sr8sNAwV2Uo1uhKLJaoliKkLqPwD/tDb8KjAeI5grsbq5W/9FY7u29gN4Nu8Rn3jsyXHA5j572sNZ4nNBIkA2UqrrPcSkhasYBnIthZO5IsHw2j7L+lv6W362N4StvVbkcHDjkfvL4qagqtcCySNj5Zm/ewhmXb0uUNNsGe2RTCWrNXWCaiNQwDCj4rXwrzZnBS4e3uH2BSAkM4fHptGXpbBB7K7d65CCx3vSqOkuU5GXOR6AUmLT75QTk7W/bHqZnCpbUrTGQucxfnPhVnTGZed/DZ8Kf0O0IxoptahUTUs9NE/4yOus= kali@kali' > /home/browser/.ssh/authorized_keys \
    && service ssh start 
RUN chmod u-s $(which passwd)

# Startup
COPY ./startup.sh /usr/bin/startup.sh
RUN chmod ugo+x /usr/bin/startup.sh
EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]