import random
import math
import numpy as np
import scipy.io.wavfile

def tanh(x):
    t = np.exp(-2*x)
    return (1-t)/(1+t)
def pycode(x):
    	n = math.ceil(x*(math.log(n2,math.e)/math.log(n1,math.e))-1)#a1
    	return n

n1=2
n2=3
play=[]
pnotes = []
ycor=[]
x=0
z=6
while x <= z:
    if x == z:
        ycor.append((n2**x/n1**pycode(x)))
        x+=1
    else:
        ycor.append((n2**x/n1**pycode(x)))
        ycor.append((n1**(pycode(x)+1)/n2**x))
        x +=1
ycor.sort()
oneoct= ycor[:]
for i in range(len(oneoct)):
    oneoct[i]= 1+oneoct[i]
twooct = ycor[:]
for i in range(len(twooct)):
    twooct[i] =2+twooct[i]
downoct = ycor[:]
downoct.reverse()
for i in range(len(downoct)):
    downoct[i]= downoct[i]**-1
pnotes.append(ycor)
pnotes.append(oneoct)
pnotes.append(twooct)
pnotes.append(downoct)
for i in pnotes:
    for n in i:
        if n not in play:
            play.append(n)
print(play)
fts = None
#fts = [0.022943,0.412962,0.548431,0.578468,0.092241,0.116378,0.052974,0.029585,0.093977,0.119660,0.064074,0.051807,0.015094,0.094184,0.015488,0.006640,0.007091,0.011557,0.043467,0.023330,0.018118,0.026921,0.010285,0.007653,0.015306,0.023175,0.013051,0.004840,0.005658,0.010814,0.014921,0.026066,0.028334,0.015227,0.010740,0.008966,0.009389,0.012547,0.011544,0.009900,0.012403,0.013093,0.008259,0.007148,0.006129,0.004932,0.004332,0.003397,0.002497,0.002241,0.002187,0.002227,0.001634,0.001186,0.001119,0.001131,0.001276,0.000970,0.001101,0.001647,0.001936,0.001632,0.001190,0.000891,0.000883,0.000906,0.000894,0.000855,0.000768,0.000721,0.000750,0.000900,0.000965,0.000844,0.000765,0.000643,0.000535,0.000464,0.000409,0.000403,0.000489,0.000642,0.000773,0.000819,0.000871,0.000930,0.000979,0.000950,0.000781,0.000649,0.000620,0.000653,0.000661,0.000706,0.000805,0.000856,0.000832,0.000793,0.000750,0.000702]

fts = [0.601382,0.263076,0.197963,0.244245,0.217992,0.114034,0.025768,0.041518,0.011954,0.006391,0.012239,0.017818,0.016819,0.012798,0.007576,0.007376,0.002891,0.021377,0.005261,0.004421,0.009226,0.004333,0.001808,0.003989,0.002078,0.001344,0.001560,0.001240,0.001586,0.001307,0.000519,0.000761,0.001009,0.000632,0.000412,0.000414,0.000361,0.000406,0.000544,0.000741,0.000281,0.000164,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000,0.000000]
#fts = [0.876155,0.188136,0.766537,0.278649,0.134428,0.143342,0.201465,0.068043,0.011284,0.021093,0.021494,0.010577,0.016431,0.007352,0.006864,0.007433,0.006500,0.004716,0.004282,0.002545,0.002718,0.002045,0.001768,0.002409,0.002409]
#fts = [0.793870,0.077609,0.047389,0.012277,0.005127,0.002760,0.002619,0.000390,0.000109,0.000105,0.000147,0.000425,0.000266,0.000201,0.000312,0.000210,0.001391,0.003570,0.001720,0.002746,0.001399,0.000749,0.000411,0.001156,0.001156]
#fts = [0.876155,0.188136,0.766537,0.278649,0.134428,0.143342,0.201465,0.068043,0.011284,0.021093,0.021494,0.010577,0.016431,0.007352,0.006864,0.007433,0.006500,0.004716,0.004282,0.002545,0.002718,0.002045,0.001768,0.002409,0.002409]
#fts = [0.793870,0.077609,0.047389,0.012277,0.005127,0.002760,0.002619,0.000390,0.000109,0.000105,0.000147,0.000425,0.000266,0.000201,0.000312,0.000210,0.001391,0.003570,0.001720,0.002746,0.001399,0.000749,0.000411,0.001156,0.001156]

timbre = []
if fts:
    for i,amp in enumerate(fts):
        overtone = i+1
        timbre += [(overtone, amp, random.uniform(0,2*math.pi))]
else:
    for overtone in range(1,10):
        amp = 1 / overtone
        timbre += [(overtone, amp,random.uniform(0,2*math.pi))]


def make_sound(freqs, sampling_freq=44100, delay=0.1, padding=2, half_life=0.5, half_lives = 8, attack=1e-2, amplitude=1, timbre = [(1,0)], variance=1/4):
    overtone_normalizer = 1 / sum(amp for _,amp,_ in timbre)
    def add_note(wf, fundfreq, start, amplitude = 0.5, phase=0, attack=1e-2):
        duration = half_life * half_lives * delay
        sample_count = math.ceil(duration*sampling_freq)
        x0 = 0
        x1 = (np.pi*2) * duration

        #note = np.sin(np.linspace(phase+x0, phase+x1, sample_count))
        note = np.zeros(sample_count)
        for overtone,amp,arg in timbre:
            #freq = fundfreq * 2**octave
            freq = fundfreq * (overtone+1)
            if freq*2 < sampling_freq:
                randamp = random.gauss(amp,amp*variance)
                note += overtone_normalizer * randamp * np.sin(np.linspace(phase+arg+x0, phase+arg+x1*freq, sample_count))

        attenuation = np.exp(np.linspace(0, -np.log(2)*half_lives, sample_count))
        attenuation *= tanh(np.linspace(0, duration/attack, sample_count))
        attenuation /= np.max(attenuation)

        note *= attenuation * amplitude
        #print(attenuation)

        i0 = math.floor(start*sampling_freq)
        i1 = min(sample_count, waveform.shape[0]-i0)
        if i1 > 0:
            waveform[i0:i0+i1] += note[:i1]


    sample_count = math.ceil(sampling_freq*((len(freqs) + (-1 + half_life * half_lives))*delay))
    waveform = np.zeros(sample_count)
    for i, f in enumerate(freqs):
        if f is not None:
            start = delay*i
            start += random.gauss(0, delay/2**6)
            start = max(start, 0)
            #add_note(waveform, f, start, amplitude = amplitude, phase=random.uniform(0, np.pi*2), attack=attack)
            add_note(waveform, f, start, amplitude = amplitude, phase=random.uniform(0, np.pi/16), attack=attack)

    return waveform

def write_waveform(outname, waveforms, sampling_freq = 44100, padding=2):
    n = 0
    for w in waveforms:
        n = max(w.shape[0], n)
    waveform = np.zeros(n+math.ceil(sampling_freq * padding))
    for w in waveforms:
        m = w.shape[0]
        for i in range(n // m):
            waveform[i * m: (i+1)*m] += w
        i = n//m
        if i*m < n:
            waveform[i*m:n] += w[:n-i*m]

        #waveform += w

    #waveform = np.array(waveform*(2**15-1), dtype=np.int16)
    waveform = np.array(tanh(waveform)*(2**15-1), dtype=np.int16)
    scipy.io.wavfile.write('mysong.wav',sampling_freq, waveform)
    print(max(waveform))
    #print(waveform.shape[0])


def make_notes(freqs, base_note=440, tempo=60, note_length=1/4, octave_base=2, octave_range=3, **kwargs):
    note_names = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']


    if len(freqs) == 0:
        return np.array([0])

    def log2(x):
        return math.log(x) / math.log(2)

    remove_sharps = True
    do_notes = True
    #do_notes = False

    min_freq = min(freqs)
    max_freq = max(freqs)
    octave_0 = log2(min_freq)
    octave_1 = log2(max_freq)
    freqs = [440*2**(octave_base-4 + octave_range * (log2(f) - octave_0) / (octave_1 - octave_0)) if f is not None else None for f in freqs]

    if do_notes:
        freqs2 = []
        octave_notes = []
        for f in freqs:
            if f is None:
                freqs2 += [None]
                continue

            octave_note = log2(f/440) + 4
            octave = math.floor(octave_note)
            note = math.floor((octave_note - octave) * 12)

            octave_notes += [(octave,note)]

        for octave, note in octave_notes:
            if '#' in note_names[note] and remove_sharps:
                note -= 1

            f2 = 440*2**((octave-4) + (note / 12))

            print(octave, note_names[note])

            freqs2 += [f2]
        freqs = freqs2

    return make_sound(freqs, delay=(60/tempo)*note_length,**kwargs)


def test_twinkle():
    notes = []
    notes += [3,3,10,10,12,24,10,None,8,8,7,7,5,5,3,None]
    notes += [10,10,8,8,7,7,5,None]
    notes += [10,10,8,8,7,7,5,None]
    notes += [3,3,10,10,12,24,10,None,8,8,7,7,5,5,3,None]

    note_names = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']

    freqs = [2*110*2**(n/12) if n is not None else None for n in notes]

    for f in freqs:
        print(f)
    #freqs = [440]
    waveform = make_sound(freqs, delay=(60/60)*(1/4), half_life=0.3,amplitude=0.5, attack=1e-3, timbre=timbre)
    write_waveform('out.wav',[waveform])


def test_random():
    values = np.random.rand(200)

    waveform = make_notes(values,timbre=timbre)
    write_waveform('out.wav',[waveform])

def test_py():
    freqs=[]
    for x in range(len(ycor)):
        freqs.append([220*ycor[x],220])
        print(ycor[x])
    waveform = make_sound(freqs, delay=(60/60)*(1/4), half_life=0.3,amplitude=0.5, attack=1e-3, timbre=timbre)
    write_waveform('out.wav',[waveform])

def test_yoursong():
    freqs=[]
    note_input=input('what notes do you want?')
    notes=note_input.split(',')
    for i in range(len(notes)):
        if int(notes[i]) == 0:
            notes[i]== None
        else:
            notes[i] = int(notes[i])
    #notes = []
    #notes += [3,3,10,10,12,12,10,None,8,8,7,7,5,5,3,None]
    #notes += [10,10,8,8,7,7,5,None]
    #notes += [10,10,8,8,7,7,5,None]
    #notes += [3,3,10,10,12,12,10,None,8,8,7,7,5,5,3,None]
    note_names = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
    for n in notes:
        if n is not None:
            freqs.append(432*play[n])
        else:
            freqs.append(None)
    #eqs = [220*play[n] if n is not None else None for n in notes]

    for f in freqs:
        print(f)

    #freqs = [440]
    waveform = make_sound(freqs, delay=(60/60)*(1/4), half_life=0.3,amplitude=0.5, attack=1e-3, timbre=timbre)
    write_waveform('out.wav',[waveform])

def main():
    #test_twinkle()
    #test_random()
    #test_py()
    test_yoursong()

main()
