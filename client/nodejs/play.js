const MidiPlayer = require('midi-player-js');

const send = require('./send')

const Player = new MidiPlayer.Player();

Player.on('midiEvent', function (event) {
    if (event.name == 'Note on') {
        send(event.noteNumber)
    }
});

// Load a MIDI file
Player.loadFile('./test.mid');
Player.play();

