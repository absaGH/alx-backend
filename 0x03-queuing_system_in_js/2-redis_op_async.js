import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

(()=> {

  client.on('error', (err) => console.log('Redis client not connected to the server: ', err));

 client.on('connect', () => console.log('Redis client connected to the server'));

})();

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

const clientget = promisify(client.get).bind(client);
const displaySchoolValue = async (schoolName) => {
    const reply = await clientget(schoolName);
    console.log(reply);
}

(async() => {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
})();
