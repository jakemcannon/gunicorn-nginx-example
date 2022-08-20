### Goal

I have failed numerous times over the years to get Flask, gunicorn, and NGINX working together. I will give it another go. Below is the order
of how I think things should be done to keep things simple.

### TODO

- [x] Get Python and Flask installed in a container
- [x] Get Flask working with gunicorn
- [x] Get gunicorn working in a container
- [x] Start implementing `docker-compose`
- [x] Finally, introduce NGINX
- [x] Get this working on AWS with a default IP
- [  ] Get NGINX working on https, port `443`
- [  ] Create an AMI
- [  ] Get this working on AWS with a subdomain
- [  ] Create an EC2 with docker and docker-compose. Then you can probably launch it every time the server startes with `user_data`

^
It's a bit more subtle here. You want docker to be able to *automatically* run in two scenarios.
1. Every time a new sever is spun up based off an image. (this is the same as the TODO above - `user_data` is only executed when an AMI launches)
2. Anytime the server crashes and reboots itself. I first found out about this in [this](https://betterprogramming.pub/how-to-use-docker-in-an-amazon-ec2-instance-5453601ec330)
post. It suggests using something called `systemctl`

# Docker usage

### Locally
```
docker-compose up -d --build --scale app=3
```

### On EC2
WIP, but for now

1. Create a new EC2 from scratch (TODO: create an AMI)
2. Manually install git, docker, docker-compose and this repo (TODO: I believe an AMI also solves this)
3. Manually set the correct user permissions for the above services and start the services (TODO: I believe an AMI also solves this)
4. Set `docker-compose` up so that if it crashes it automatically reboots
5. Figure out the correct commands for `user_data` and spin up a new EC2 to test

