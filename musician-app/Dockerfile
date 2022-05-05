FROM node:8-alpine
RUN apk update && apk add tzdata
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN date

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

RUN mkdir -p /usr/src/app
RUN chown -R appuser:appgroup /usr/src/app
WORKDIR /usr/src/app
USER appuser
COPY package*.json ./
RUN npm install
COPY --chown=appuser:appgroup . .
EXPOSE 3001
CMD [ "node", "app.js" ]
