# Use an official Nginx runtime as the base image
FROM nginx:latest

# Copy the configuration file for Nginx
COPY default.conf /etc/nginx/conf.d/default.conf
COPY ./letsencrypt /etc/letsencrypt/

# Copy the built Svelte application to the Nginx container
COPY build/ /usr/share/nginx/html

# Expose port 80
EXPOSE 80 443

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]