from pathlib import Path
p=Path('index.html')
s=p.read_text()
old="try{speechSynthesis.cancel();let u=new SpeechSynthesisUtterance(t);"
new="try{speechSynthesis.cancel();try{speechSynthesis.resume()}catch(e){}let u=new SpeechSynthesisUtterance(t);"
if old not in s:
    raise SystemExit('speak() target not found')
s=s.replace(old,new,1)
# iPhone Safari is more reliable when speech requested from a tap is started immediately,
# rather than after a timer that loses the user-activation context.
old="if(announce&&p.voice)setTimeout(()=>speak(r?greet()+' Heading to '+r+'?':greet()+' Where are you going?',false,p.voiceStyle,()=>{if(p.micEnabled)setTimeout(()=>rearmVoice('home'),180)}),250);"
new="if(announce&&p.voice)speak(r?greet()+' Heading to '+r+'?':greet()+' Where are you going?',false,p.voiceStyle,()=>{if(p.micEnabled)setTimeout(()=>rearmVoice('home'),180)});"
if old not in s:
    raise SystemExit('home speech target not found')
s=s.replace(old,new,1)
old="if(tripVoice)setTimeout(()=>speak('Route '+r.id+' selected. Continue straight for 1.2 kilometres.',false,p.voiceStyle,()=>{if(byVoice||voiceFlow)setTimeout(()=>startListen('navigation',navMic,true),200)}),250)"
new="if(tripVoice)speak('Route '+r.id+' selected. Continue straight for 1.2 kilometres.',false,p.voiceStyle,()=>{if(byVoice||voiceFlow)setTimeout(()=>startListen('navigation',navMic,true),200)})"
if old not in s:
    raise SystemExit('navigation speech target not found')
s=s.replace(old,new,1)
# Warm the system voice list when the user explicitly enables speaker guidance.
old="function toggleOnboardSpeaker(){p.voice=!p.voice;onboardSpeaker.textContent=p.voice?'ON':'OFF'}"
new="function toggleOnboardSpeaker(){p.voice=!p.voice;onboardSpeaker.textContent=p.voice?'ON':'OFF';if(p.voice){try{speechSynthesis.getVoices();speechSynthesis.resume()}catch(e){}}}"
if old not in s:
    raise SystemExit('speaker toggle target not found')
s=s.replace(old,new,1)
p.write_text(s)
print('NaVue iPhone system-voice repair applied')
# one-time execution trigger
