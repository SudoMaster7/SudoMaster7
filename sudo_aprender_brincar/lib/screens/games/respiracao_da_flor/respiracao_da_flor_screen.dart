import 'package:flutter/material.dart';
import 'dart:async';

class RespiracaoDaFlorScreen extends StatefulWidget {
  const RespiracaoDaFlorScreen({super.key});

  @override
  State<RespiracaoDaFlorScreen> createState() => _RespiracaoDaFlorScreenState();
}

class _RespiracaoDaFlorScreenState extends State<RespiracaoDaFlorScreen>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _animation;

  String _instruction = "Clique em Iniciar";
  bool _isPlaying = false;
  int _cycleCount = 0;
  final int _maxCycles = 5; // Number of breath cycles

  // Durations for inhale and exhale
  final Duration _inhaleDuration = const Duration(seconds: 4);
  final Duration _exhaleDuration = const Duration(seconds: 6);
  // Hold duration can be added if needed: const Duration(seconds: 2);

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: _inhaleDuration, // Initial duration for inhale
    );

    _animation = Tween<double>(begin: 50.0, end: 150.0).animate(
      CurvedAnimation(parent: _controller, curve: Curves.easeInOut),
    )..addListener(() {
        setState(() {});
      });

    _controller.addStatusListener((status) {
      if (status == AnimationStatus.completed) {
        if (_controller.duration == _inhaleDuration) { // Finished inhaling
          setState(() => _instruction = "Segure..."); // Optional hold instruction
          // Start exhaling after a brief pause (or immediately)
          Timer(const Duration(milliseconds: 500), () { // Simulate hold
             if (!_isPlaying) return; // Stop if animation was cancelled
            setState(() => _instruction = "Expire Lentamente...");
            _controller.duration = _exhaleDuration;
            _controller.reverse();
          });
        }
      } else if (status == AnimationStatus.dismissed) { // Finished exhaling
        _cycleCount++;
        if (_cycleCount < _maxCycles && _isPlaying) {
          setState(() => _instruction = "Inspire Profundamente...");
          _controller.duration = _inhaleDuration;
          _controller.forward();
        } else {
          _stopAnimation();
          setState(() => _instruction = "Muito bem! Sessão completa.");
        }
      }
    });
  }

  void _startAnimation() {
    if (_isPlaying) return;
    _cycleCount = 0;
    _isPlaying = true;
    setState(() => _instruction = "Inspire Profundamente...");
    _controller.duration = _inhaleDuration;
    _controller.forward();
  }

  void _stopAnimation() {
    _isPlaying = false;
    _controller.stop();
     setState(() {
      _instruction = _cycleCount >= _maxCycles ? "Muito bem! Sessão completa." : "Clique em Iniciar";
      // Reset to initial size if stopped prematurely
      if (_controller.value != 0.0 && _cycleCount < _maxCycles) {
          _controller.animateTo(0.0, duration: const Duration(milliseconds: 300)); // Added const
      }
    });
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Jogo: Respiração da Flor (MVP)'),
        leading: IconButton(
          icon: const Icon(Icons.close),
          onPressed: () {
            _stopAnimation(); // Stop animation before popping
            if (Navigator.canPop(context)) Navigator.pop(context);
          },
        ),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              _instruction,
              style: const TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: 50),
            // Animated "Flower" (a simple circle for MVP)
            Container(
              width: _animation.value * 1.5, // Diameter increased slightly for better visual
              height: _animation.value * 1.5, // Diameter increased slightly for better visual
              decoration: BoxDecoration(
                color: Colors.pinkAccent.withOpacity(_controller.status == AnimationStatus.reverse ? (_animation.value /150.0 * 0.5) + 0.2 : (_animation.value /150.0 * 0.7) + 0.3 ), // Opacity change
                shape: BoxShape.circle,
                 boxShadow: [
                  BoxShadow(
                    color: Colors.pink.withAlpha(100),
                    blurRadius: _animation.value / 20.0, // Dynamic blur
                    spreadRadius: _animation.value / 30.0, // Dynamic spread
                  )
                ],
              ),
              // Child could be an actual flower image that scales
            ),
            const SizedBox(height: 70),
            if (!_isPlaying || _cycleCount >= _maxCycles)
              ElevatedButton(
                onPressed: _startAnimation,
                style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(horizontal: 30, vertical: 15)),
                child: const Text('Iniciar', style: TextStyle(fontSize: 18)),
              )
            else
              ElevatedButton(
                onPressed: _stopAnimation,
                 style: ElevatedButton.styleFrom(backgroundColor: Colors.red, padding: const EdgeInsets.symmetric(horizontal: 30, vertical: 15)),
                child: const Text('Parar', style: TextStyle(fontSize: 18)),
              ),
            const SizedBox(height: 20),
             ElevatedButton(
                onPressed: () {
                  _stopAnimation();
                  if (Navigator.canPop(context)) Navigator.pop(context);
                },
                child: const Text('Voltar ao Lobby'),
            ),
          ],
        ),
      ),
    );
  }
}
