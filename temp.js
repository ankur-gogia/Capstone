const [code, setCode] = useState('');

const submitCode = () => {
    fetch('http://localhost:8080/api/code/submit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ code }),
    })
      .then(response => response.json())
      .then(data => {
        console.log('Response from server:', data);
      })
      .catch(error => {
        console.error('Error submitting code:', error);
      });
  };

  setCode(`public class HelloWorld {public static void main(String[] args) {System.out.println("Hello, World!");}}")