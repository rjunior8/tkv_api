FROM nginx:1.21.4

RUN mkdir -p /etc/nginx/ssl/

RUN rm /etc/nginx/conf.d/default.conf

COPY ./nginx.conf /etc/nginx/conf.d/default.conf

USER root

RUN chown -R nginx:nginx /var/cache/nginx/ /var/run/ /var/log/nginx/ /etc/nginx/ssl/
RUN chmod -R 755 /var/cache/nginx/ /var/run/ /var/log/nginx/ /etc/nginx/ssl/

USER nginx
