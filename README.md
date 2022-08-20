### Goal

I have failed numerous times over the years to get Flask, gunicorn, and NGINX working together. I will give it another go. Below is the order
of how I think things should be done to keep things simple.

### TODO

- [x] Get Python and Flask installed in a container
- [x] Get Flask working with gunicorn
- [x] Get gunicorn working in a container
- [x] Start implementing `docker-compose`
- [] Finally, introduce NGINX

- [] Get this working on AWS with a default IP
- [] Get this working on AWS with a subdomain


### Docker useage

There was some struggling with getting the domain to be accessible. I finally got it to work with the command below. Additionally, It was
important that `--host=0.0.0.0` was in the Dockerfile when running flask. Essentially this `flask run --host=0.0.0.0` command if you were running
the flask server locally. I'm not sure of the signifigance of this and how it will work with NGINX as well as a domain on AWS.


```
docker run -p 5000:5000 flask-deployment-demo
```
