import redis from 'redis';

const client = redis.createClient();

(()=> {

  client.on('error', (err) => console.log('Redis client not connected to the server: ', err));

 client.on('connect', () => console.log('Redis client connected to the server'));

})();

function setNewSchool() {
    client.HSET('HolbertonSchools', 'Portland', 50, (error, reply) => redis.print(`Reply: ${reply}`));
    client.HSET('HolbertonSchools', 'Seattle', 80, (error, reply) => redis.print(`Reply: ${reply}`));
    client.HSET('HolbertonSchools', 'New York', 20, (error, reply) => redis.print(`Reply: ${reply}`));
    client.HSET('HolbertonSchools', 'Bogota', 20, (error, reply) => redis.print(`Reply: ${reply}`));
    client.HSET('HolbertonSchools', 'Cali', 40, (error, reply) => redis.print(`Reply: ${reply}`));
    client.HSET('HolbertonSchools', 'Paris', 2, (error, reply) => redis.print(`Reply: ${reply}`));
    client.hgetall('HolbertonSchools', (err, reply) => {
        console.log(reply);
    });
}

setNewSchool();
