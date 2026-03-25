import http from 'k6/http';
import { check, sleep } from 'k6';

/*export let options = {
  vus: 10,          // 10 Nutzer gleichzeitig
  duration: '10s',  // 10 Sekunden
};*/

/*export let options = {
  vus: 50, // 50 Nutzer gleichzeitig
  duration: '30s', // 30 Sekunden
};*/

export let options = {
  stages: [
    { duration: '10s', target: 10 },
    { duration: '20s', target: 50 },
    { duration: '10s', target: 0 },
  ],
};

export default function () {
  let res = http.get('https://jsonplaceholder.typicode.com/posts');

  check(res, {
    'status is 200': (r) => r.status === 200,
    'response time < 500ms': (r) => r.timings.duration < 500,
  });

  sleep(1);
}

