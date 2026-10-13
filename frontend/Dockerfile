from node

workdir /app

copy package*.json ./
RUN npm install

copy server.js ./
copy public ./public

ENV NODE_ENV=production
ENV PORT=3000

EXPOSE 3000

CMD ["node", "server.js"]