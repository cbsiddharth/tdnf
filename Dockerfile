FROM photon:latest

MAINTAINER csiddharth@vmware.com

RUN tdnf update  -q -y
RUN tdnf remove  -q -y toybox
RUN tdnf install -q -y build-essential cmake curl-devel rpm-build libsolv-devel \
                       popt-devel sed git createrepo_c glib libxml2 findutils \
                       python3 python3-pip python3-setuptools python3-devel

# python build/test dependencies
RUN pip3 install -q requests urllib3 pyOpenSSL pytest

CMD ["/bin/bash"]
