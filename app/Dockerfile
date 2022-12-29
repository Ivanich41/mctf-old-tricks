FROM ubuntu:22.04

# Installs
RUN apt-get update  \
    && apt install -y vim openssh-server socat links
RUN adduser --disabled-password --gecos "" browser

# SSH Config
RUN groupadd sshgroup && usermod -aG sshgroup browser
RUN mkdir /var/run/sshd
RUN echo 'root:N0tRequ1r3d' | chpasswd
RUN echo 'browser:1234' | chpasswd
COPY ./sshd_config /etc/ssh/sshd_confog
COPY ./startup.sh /usr/bin/startup.sh
RUN chmod ugo+x /usr/bin/startup.sh
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN mkdir /home/browser/.ssh \
    && echo 'command="/usr/bin/startup.sh" ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDhZgdSFMi+HwijNU1bQBCJN1ecF7AeZ4/YoALdNQ8mTDITP15Y3Ld5jb2ZIelZ+20QQEdwImQKyNMJDhBduIh6Xz+J9C1b2NLEA6nK1gU/+HR1R+fJ6O3OShVxV9/ItJrPEb+rY/P7OK6Feyi8p7UXgH1M8I7RsJJNQ69XiAoJbaO5+jCQPG2EqDgBBSzLGLf05KE3OyOOnNROEqnyZHX/HC6frgtZGMfNm3Hk+aEkIoRI8Pag0HQAphnBdIcJzokjfAVmzoDT+3EjhkXXec/1mUd4ckD1aJ3MMnx2h8fJHp9lIl9EjNcX+YJaISoX1BdCwbWihAhfRv27ZTnWd9JQ0bj6wVj4WfGDjIODOVrx0EB6dlbpBAOvczXxpG8BeYRSBBjy1mW5cDjZQr96ZB0rp2j8P8oTf3H9VFXQV0fOilZOVYlspXnLG2RdpDEjV//KUpkNDCgfAQOcEh/VKUaQZV+PxR4DpBB+y4Qtw6nqSxr6TnnEslZ/3vz3TOieis8= kali@kali' > /home/browser/.ssh/authorized_keys \
    && service ssh start \
    && chmod u-s $(which passwd)

# Startup
EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]