import redis from 'redis';
import kue from 'kue';

const client = redis.createClient();

const jobInfo = {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
};

const push_notification_code = kue.createQueue();

(()=> {

  client.on('error', (err) => console.log('Redis client not connected to the server: ', err));

  client.on('connect', () => console.log('Redis client connected to the server'));

})();

const job = push_notification_code.create(jobInfo).save( (err) => {
   if( !err ) console.log( `Notification job created: ${job.id}` );
});

job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'));
