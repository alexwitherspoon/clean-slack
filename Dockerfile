# clean-slack
# https://github.com/alexwitherspoon/clean-slack
FROM debian:stable

MAINTAINER Alex Witherspoon <alex@alexwitherspoon.com>

# Commands to Stage OS
RUN echo "Installing Base Utilties" && \
    bash -c "apt-get update -qq" && \
    bash -c "apt-get install -qq --force-yes python sudo curl cron git" && \
    bash -c "echo 'root:clean-slack' | chpasswd" && \
    bash -c "apt-get autoremove -qq --force-yes" && \
    bash -c "apt-get clean -qq --force-yes" && \
    echo "Base Utilities Installed" && \
    echo "...."

RUN echo "Installing clean-slack app" && \
    bash -c "git clone https://github.com/alexwitherspoon/clean-slack.git /opt/clean-slack" && \
    bash -c "crontab /opt/clean-slack/clean-slack.cron" && \
    bash -c "chmod +x /opt/clean-slack/clean-slack.py" && \
    bash -c "touch /var/log/clean-slack.log" && \
    echo "clean-slack app" && \
    echo "...."

# Commands to Run App
CMD bash -c "cron" && \
bash -c "sleep 1d"
