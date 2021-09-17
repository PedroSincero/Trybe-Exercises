// HEADER

// {
//   "alg": "HS256",
//   "typ": "JWT"
// }

// PAYLOAD (DADOS DO USUARIO)

// {
//   "sub": "1234567890",
//   "name": "John Doe",
//   "admin": true
// }

// SIGNATURE

// Para gerar a assinatura, você deve usar o header e o payload codificados em base64 , usando o algoritmo definido no header:
// EX:
import {
  hmac
} from 'bibliotecaDeHmac';

function base64(string) {
  return Buffer.from(string).toString('base64');
}

const header = JSON.stringify({
  alg: 'HS256',
  type: 'JWT'
});

const payload = JSON.stringify({
  sub: '1234567890',
  name: 'John Doe',
  admin: true
});

const secret = 'MinhaSenhaMuitoComplexa123';

const assinatura = hmac(`${base64(header)}.${base64(payload)}`, secret);

const token = `${base64(header)}.${base64(payload)}.${base64(assinatura)}`;

// Exemplo de resultado:

// eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXIxIiwiZXhwIjoxNTQ3OTc0MDgyfQ.2Ye5_w1z3zpD4dSGdRp3s98ZipCNQqmsHRB9vioOx54

// Nesse caso, temos:

// Header: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
// Payload: eyJ1c2VybmFtZSI6InVzZXIxIiwiZXhwIjoxNTQ3OTc0MDgyfQ
// Signature: 2Ye5_w1z3zpD4dSGdRp3s98ZipCNQqmsHRB9vioOx54
