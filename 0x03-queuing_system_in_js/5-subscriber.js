import redis from 'redis';

const subscriber = redis.createClient();

(()=> {

  subscriber.on('error', (err) => console.log('Redis client not connected to the server: ', err));

  subscriber.on('connect', () => console.log('Redis client connected to the server'));

})();

const channel = 'holberton school channel';

subscriber.subscribe(channel, (error, channel) => {
  if (error) {
      throw new Error(error);
  }
});

subscriber.on('message', (channel, message) => {
    if (message != 'KILL_SERVER') {
	console.log(`${message}`);
    } else {
	console.log(`${message}`);
	subscriber.unsubscribe();
	subscriber.end(true);
    }
});

