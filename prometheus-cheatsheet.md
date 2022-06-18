# Prometheus Cheat Sheet/Notes <a id ='top'></a>

<br>
<br>

# Contents

- [Install Prometheus on on UBuntu Linux](#1)
- [Intall Node Exporter on Ubuntu Linux](#2)
- [Configure Prometheus to Auto-Detect Ec2 Instances](#3)
- [](#4)
- [](#5)
- [](#6)
- [](#7)
- [](#8)
- [](#9)
- [](#10)
- [](#11)
- [](#12)
- [](#13)
- [](#14)
- [](#15)
- [](#16)
- [](#17)
- [](#18)
- [](#19)
- [](#20)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [go to top](#top)

<br>
<br>
<br>

# Install Prometheous on Ubuntu Linux <a id='1'></a> ([go to top](#top))

- [Guide](https://codewizardly.com/prometheus-on-aws-ec2-part1/)
- Open ports 9090, 9100
- ssh into Instance

  ```
  sudo useradd --no-create-home prometheus
  sudo mkdir /etc/prometheus
  sudo mkdir /var/lib/prometheus

  wget https://github.com/prometheus/prometheus/releases/download/v2.19.0/prometheus-2.19.0.linux-amd64.tar.gz
  tar xvfz prometheus-2.19.0.linux-amd64.tar.gz
  rm -rf prometheus-2.19.0.linux-amd64.tar.gz

  sudo cp prometheus-2.19.0.linux-amd64/prometheus /usr/local/bin
  sudo cp prometheus-2.19.0.linux-amd64/promtool /usr/local/bin/
  sudo cp -r prometheus-2.19.0.linux-amd64/consoles /etc/prometheus
  sudo cp -r prometheus-2.19.0.linux-amd64/console_libraries /etc/prometheus
  sudo cp prometheus-2.19.0.linux-amd64/prometheus.yml /etc/prometheus

  sudo touch /etc/systemd/system/prometheus.service
  sudo vim /etc/systemd/system/prometheus.service
  ```

  - insert the following command text to make prometheus available as a service and boot with the OS upon restart

  ```
  [Unit]
  Description=Prometheus
  Wants=network-online.target
  After=network-online.target

  [Service]
  User=prometheus
  Group=prometheus
  Type=simple
  ExecStart=/usr/local/bin/prometheus \
      --config.file /etc/prometheus/prometheus.yml \
      --storage.tsdb.path /var/lib/prometheus/ \
      --web.console.templates=/etc/prometheus/consoles \
      --web.console.libraries=/etc/prometheus/console_libraries

  [Install]
  WantedBy=multi-user.target
  ```

  ```
  sudo chown prometheus:prometheus /etc/prometheus
  sudo chown prometheus:prometheus /usr/local/bin/prometheus
  sudo chown prometheus:prometheus /usr/local/bin/promtool
  sudo chown -R prometheus:prometheus /etc/prometheus/consoles
  sudo chown -R prometheus:prometheus /etc/prometheus/console_libraries
  sudo chown -R prometheus:prometheus /var/lib/prometheus
  ```

  ```
  sudo systemctl daemon-reload
  sudo systemctl enable prometheus
  prometheus --config.file=/etc/prometheus/prometheus.yml
  ```

  - visit prometheous

  ```
  http://ec2-34-226-147-0.compute-1.amazonaws.com:9090
  ```

<br>
<br>
<br>

# Intall Node Exporter on Ubuntu EC2 <a id='2'></a> ([go to top](#top))

- [Guide](https://codewizardly.com/prometheus-on-aws-ec2-part2/)
- Open ports 9090, 9100

  ```
  sudo useradd --no-create-home node_exporter
  wget https://github.com/prometheus/node_exporter/releases/download/v1.0.1/node_exporter-1.0.1.linux-amd64.tar.gz
  tar xzf node_exporter-1.0.1.linux-amd64.tar.gz
  sudo cp node_exporter-1.0.1.linux-amd64/node_exporter /usr/local/bin/node_exporter
  rm -rf node_exporter-1.0.1.linux-amd64.tar.gz node_exporter-1.0.1.linux-amd64

  sudo touch /etc/systemd/system/node-exporter.service
  sudo vim /etc/systemd/system/node-exporter.service
  ```

  - insert the following command text to make node_exporter available as a service and boot with the OS upon restart

  ```
  [Unit]
  Description=Prometheus Node Exporter Service
  After=network.target

  [Service]
  User=node_exporter
  Group=node_exporter
  Type=simple
  ExecStart=/usr/local/bin/node_exporter

  [Install]
  WantedBy=multi-user.target
  ```

  ```
  sudo systemctl daemon-reload
  sudo systemctl enable node-exporter
  sudo systemctl start node-exporter
  sudo systemctl status node-exporter
  ```

  - On the prometheous serves, edit the /etc/prometheus/prometheus.yml file

  ```
  To Myself, [6/6/2022 8:06 PM]
  # my global config
  global:
    scrape_interval:     15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
    evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
    # scrape_timeout is set to the global default (10s).
    external_labels:
      monitor: 'prometheus'

  # Alertmanager configuration
  alerting:
    alertmanagers:
    - static_configs:
      - targets:
        # - alertmanager:9093

  # Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
  rule_files:
    # - "first_rules.yml"
    # - "second_rules.yml"

  # A scrape configuration containing exactly one endpoint to scrape:
  # Here it's Prometheus itself.
  scrape_configs:
    # The job name is added as a label job=<job_name> to any timeseries scraped from this config.
    - job_name: 'prometheus'

      # metrics_path defaults to '/metrics'
      # scheme defaults to 'http'.

      static_configs:
      - targets: ['localhost:9090']

    - job_name: 'node_exporter'

      static_configs:

        - targets: ['ec2-34-203-245-35.compute-1.amazonaws.com:9100']
  ```

  ```
  sudo systemctl restart prometheus
  alertmanager --config.file=/etc/prometheus/alertmanager.yml
  ```

  ```
  http://ec2-34-226-147-0.compute-1.amazonaws.com:9090/targets
  http://ec2-34-203-245-35.compute-1.amazonaws.com:9100
  ```

<br>
<br>
<br>

# Configure Prometheus to Auto-Detect Ec2 Instances <a id='3'></a> ([go to top](#top))

- [Guide](https://codewizardly.com/prometheus-on-aws-ec2-part3/)

<br>
<br>
<br>

# SetUp Prometheus Alerts <a id=''></a> ([go to top](#top))

- [Guide](https://codewizardly.com/prometheus-on-aws-ec2-part4/)

```
wget https://github.com/prometheus/alertmanager/releases/download/v0.21.0/alertmanager-0.21.0.linux-amd64.tar.gz
tar xvfz alertmanager-0.21.0.linux-amd64.tar.gz
sudo cp alertmanager-0.21.0.linux-amd64/alertmanager /usr/local/bin
sudo cp alertmanager-0.21.0.linux-amd64/amtool /usr/local/bin/
 sudo mkdir /var/lib/alertmanager
sudo cp alertmanager-0.21.0.linux-amd64/alertmanager.yml /etc/prometheus/alertmanager.yml


```

```
route:
group_by: [Alertname]
receiver: email-me

receivers:

- name: email-me
  email_configs:
  - to: EMAIL_YO_WANT_TO_SEND_EMAILS_TO
    from: YOUR_EMAIL_ADDRESS
    smarthost: smtp.gmail.com:587
    auth_username: email@gmail.com
    auth_identity: email@gmail.com
    auth_password: emai-password
```

```
sudo vim /etc/systemd/system/alertmanager.servi
```

```
[Unit]
Description=Alert Manager
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
User=prometheus
Group=prometheus
ExecStart=/usr/local/bin/alertmanager \
 --config.file=/etc/prometheus/alertmanager.yml \
 --storage.path=/var/lib/alertmanager

Restart=always

[Install]
WantedBy=multi-user.target
```

```
sudo systemctl daemon-reload
sudo systemctl enable alertmanager
sudo systemctl start alertmanager

sudo vim /etc/prometheus/rules.yml

groups:

- name: Down
  rules:
  - alert: InstanceDown
    expr: up == 0
    for: 3m
    labels:
    severity: 'critical'
    annotations:
    summary: "Instance {{$labels.instance}} is down"
    description: " of job has been down for more than 3 minutes."

sudo chown -R prometheus:prometheus /etc/prometheus

sudo vim /etc/prometheus/prometheus.yml
```

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

```

```
