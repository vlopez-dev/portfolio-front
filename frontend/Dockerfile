FROM node:18 as builder

WORKDIR /app

COPY package*.json ./
RUN npm install --save-dev svelte-feather-icons

RUN npm install

COPY . .

RUN npm run build

# Final stage
FROM node:18-alpine

WORKDIR /app

COPY --from=builder /app .

EXPOSE 80

CMD ["npm", "run", "start"]