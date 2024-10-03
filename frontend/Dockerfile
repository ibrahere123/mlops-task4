FROM node:14-alpine

# Set the working directory.
WORKDIR /usr/src/app

# Copy package.json and install dependencies.
COPY package*.json ./
RUN npm install -g http-server  # Ensure http-server is installed globally
RUN npm install

# Copy the rest of the application code.
COPY . .

# Expose the port the app runs on.
EXPOSE 3000

# Command to run the app.
CMD ["npx", "http-server", "-p", "3000"]
