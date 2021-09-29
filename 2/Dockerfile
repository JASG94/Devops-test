FROM python:3.9.7-slim

LABEL maintainer = "Javier Salvador García  <javiersalvadorgarcia94@gmail.com>"

# Update and clean SO
RUN apt-get update \
    && apt-get -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" upgrade -yq \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install framework
RUN pip3 install flask 

# Copy python code
COPY 1/simple_API.py /simple_API.py

# Expose flask port
EXPOSE 5000

# Execute python code
CMD [ "python", "-u", "/simple_API.py" ]