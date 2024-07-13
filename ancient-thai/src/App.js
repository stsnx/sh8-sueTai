import React, { useState,useEffect } from 'react';
import audioFile from './resources/kazuya.mp3';
import './App.css';

function App() {
  const [displayText, setDisplayText] = useState('');
  const audioRef = React.useRef(null);
  useEffect(() => {
    const playPromise = audioRef.current.play();

    // Handling autoplay failure due to browser policies
    if (playPromise !== undefined) {
      playPromise.catch(error => {
        console.error('Autoplay was prevented:', error);
      });
    }
  }, [displayText]);
  
  const handleChange =async (e) => {
    if (displayText != '') {
      e.preventDefault();
      try {
            
            const response = await fetch('http://localhost:5000/api/update-text', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({ text: e.target.value }),
            })
            if (!response.ok) {
              throw new Error('Network response was not ok');
            }
            const data = await response.json();
            setDisplayText(data.text);
          } catch (error) {
            console.error('Error:', error);
          }
        }
    else{
      setDisplayText(e.target.value);
    }
  }
  return (
    <div class="bg-fixed h-[100vh] w-[100vw] grid content-center pt-[30vh] )]" 
      style={{ backgroundImage: `url('https://media.discordapp.net/attachments/733998115639787551/1261783893263122443/Thynk_Unlimited_1.png?ex=66943752&is=6692e5d2&hm=462298064f6a062fbb69474e50b50bcfe78bb681380f5a82b5943a0e40632cc8&=&format=webp&quality=lossless&width=605&height=339')` ,
      backgroundSize: 'cover',
      backgroundRepeat: 'no-repeat',}}>
        <audio ref={audioRef} src={audioFile} loop autoPlay />
        <div class="text-4xl place-self-center mb-[3vh] border-2 border-black rounded-lg">
          <textarea 
          class="h-[25vh] w-[50vw] p-4"
          placeholder="พิมพ์ภาษาของท่าน"
          onChange={handleChange} />
        </div>
        <div class="font-laisuethai text-6xl font-bold place-self-center">
          <div class="h-[25vh] w-[50vw] p-4 border-2 border-black bg-white rounded-lg">{displayText}</div>
          {/* <textarea 
          class="h-[25vh] w-[50vw] p-4"
          value={displayText}
          //onChange={handleChange} 
          /> */}
        </div>
    </div>
  );
}

export default App;
