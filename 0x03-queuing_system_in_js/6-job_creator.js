import kue from 'kue';

const jobInfo = {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
};

const q = kue.createQueue();

const job = q.create('push_notification_code', jobInfo).save( (err) => {
   if( !err ) console.log( `Notification job created: ${job.id}` );
});

job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'));
