import axios from 'axios';

export const getRaceData = async () => {
  return await axios.get('http://localhost:8000/race-data', {
    // Any auth goes here.
  });
}
