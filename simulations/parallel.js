const { spawn } = require('child_process');

const spawner = require('child_process').spawn;

// string
//const data_to_pass_in = 'Send this to python script';

// array
//const data_to_pass_in = ['Send this to python script'];

// object
const data_to_pass_in = {
  data_sent: 'Send this to python script.',
  data_returned: undefined,
}

console.log('Data sent to python script', data_to_pass_in);


// command to run, array containing path & data
const python_process = spawner('python', ['./RNG.py', JSON.stringify(data_to_pass_in)])

python_process.stdout.on('data', (data) => {
  console.log('Data recieved from python script', JSON.parse(data.toString()));
})


