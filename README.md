### Goal

I have failed numerous times over the years to get Flask, gunicorn, and NGINX working together. I will give it another go. Below is the order
of how I think things should be done to keep things simple.

### TODO

- [x] Get Python and Flask installed in a container
- [x] Get Flask working with gunicorn
- [x] Get gunicorn working in a container
- [x] Start implementing `docker-compose`
- [x] Finally, introduce NGINX

- [] Get NGINX working on https, port `443`
- [] Get this working on AWS with a default IP
- [] Get this working on AWS with a subdomain

- [] Create an EC2 with docker and docker-compose. Then you can probably launch it every time the server startes with `user_data`

^
It's a bit more subtle here. You want docker to be able to *automatically* run in two scenarios.
1. Every time a new sever is spun up based off an image. (this is the same as the TODO above - `user_data` is only executed when an AMI launches)
2. Anytime the server crashes and reboots itself. I first found out about this in [this](https://betterprogramming.pub/how-to-use-docker-in-an-amazon-ec2-instance-5453601ec330)
post. It suggests using something called `systemctl`


### Docker useage

There was some struggling with getting the domain to be accessible. I finally got it to work with the command below. Additionally, It was
important that `--host=0.0.0.0` was in the Dockerfile when running flask. Essentially this `flask run --host=0.0.0.0` command if you were running
the flask server locally. I'm not sure of the signifigance of this and how it will work with NGINX as well as a domain on AWS.


```
docker run -p 5000:5000 flask-deployment-demo
```

