import 'package:flutter/material.dart';
import 'dart:ui'; // Required for PointMode

class ConecteOsPontosScreen extends StatefulWidget {
  const ConecteOsPontosScreen({super.key});

  @override
  State<ConecteOsPontosScreen> createState() => _ConecteOsPontosScreenState();
}

class _ConecteOsPontosScreenState extends State<ConecteOsPontosScreen> {
  // MVP: Fixed points for a simple shape (e.g., a square or triangle)
  final List<Offset> _points = [
    const Offset(100, 100),
    const Offset(200, 100),
    const Offset(200, 200),
    const Offset(100, 200),
  ];

  final List<int> _connectedPointIndices = []; // Stores the actual indices of the points in _points list
  bool _isCompleted = false;

  void _handlePointTap(int tappedIndex) {
    if (_isCompleted) return;

    setState(() {
      if (_connectedPointIndices.isEmpty) {
        // Rule: Must start with point 0 (labeled "1")
        if (tappedIndex == 0) {
          _connectedPointIndices.add(tappedIndex);
        }
      } else {
        // Rule: Must tap the next point in sequence
        int expectedNextOriginalIndex = _connectedPointIndices.last + 1;
        if (tappedIndex == expectedNextOriginalIndex && !_connectedPointIndices.contains(tappedIndex)) {
          _connectedPointIndices.add(tappedIndex);
        }
        // Check for completion: all points connected in sequence
        if (_connectedPointIndices.length == _points.length) {
          _isCompleted = true;
          // Optional: Automatically add the line back to the start to close the shape
          // _connectedPointIndices.add(_connectedPointIndices.first); // This creates a line segment
        }
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Jogo: Conecte os Pontos (MVP)'),
         leading: IconButton(
          icon: const Icon(Icons.close),
          onPressed: () {
             if (Navigator.canPop(context)) Navigator.pop(context);
          },
        ),
      ),
      body: Column(
        children: [
          Expanded(
            child: CustomPaint(
              painter: _ConnectTheDotsPainter(points: _points, connectedOriginalIndices: _connectedPointIndices, isCompleted: _isCompleted),
              child: SizedBox( // Use SizedBox to constrain CustomPaint, or it might be zero-sized
                width: double.infinity,
                height: double.infinity,
                child: Stack(
                  children: List.generate(_points.length, (index) {
                    bool isConnected = _connectedPointIndices.contains(index);
                    bool isNextExpected = false;
                    if (!_isCompleted && _connectedPointIndices.isNotEmpty) {
                        isNextExpected = (index == _connectedPointIndices.last + 1);
                    } else if (!_isCompleted && _connectedPointIndices.isEmpty) {
                        isNextExpected = (index == 0);
                    }


                    return Positioned(
                      left: _points[index].dx - 20, // Adjust for tap area size
                      top: _points[index].dy - 20,  // Adjust for tap area size
                      child: GestureDetector(
                        onTap: () => _handlePointTap(index),
                        child: Container(
                          width: 40,
                          height: 40,
                          decoration: BoxDecoration(
                            color: isConnected ? Colors.green.withOpacity(0.7) : (isNextExpected ? Colors.yellow.withOpacity(0.7) : Colors.blue.withOpacity(0.5)),
                            shape: BoxShape.circle,
                            border: Border.all(color: isNextExpected ? Colors.orange : Colors.transparent, width: 2)
                          ),
                          child: Center(child: Text('${index + 1}', style: const TextStyle(fontWeight: FontWeight.bold))),
                        ),
                      ),
                    );
                  }),
                ),
              ),
            ),
          ),
          if (_isCompleted)
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                children: [
                  const Text('Parabéns, você conectou todos os pontos!', style: TextStyle(fontSize: 20, color: Colors.green)),
                  const SizedBox(height:10),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      ElevatedButton(
                        onPressed: () {
                          setState(() {
                            _connectedPointIndices.clear();
                            _isCompleted = false;
                          });
                        },
                        child: const Text('Jogar Novamente'),
                      ),
                       ElevatedButton(
                        onPressed: () {
                          if (Navigator.canPop(context)) Navigator.pop(context);
                        },
                        child: const Text('Voltar ao Lobby'),
                      ),
                    ],
                  ),
                ],
              ),
            ),
           if (!_isCompleted)
             Padding(
               padding: const EdgeInsets.all(16.0),
               child: Text(
                 _connectedPointIndices.isEmpty ?
                 'Toque no ponto "1" para começar.' :
                 'Toque no próximo ponto para continuar. \nConectados: ${_connectedPointIndices.length}/${_points.length}',
                 style: const TextStyle(fontSize: 16),
                 textAlign: TextAlign.center,
               ),
             )
        ],
      ),
    );
  }
}

class _ConnectTheDotsPainter extends CustomPainter {
  final List<Offset> points;
  final List<int> connectedOriginalIndices; // These are actual indices from the  list
  final bool isCompleted;

  _ConnectTheDotsPainter({required this.points, required this.connectedOriginalIndices, required this.isCompleted});

  @override
  void paint(Canvas canvas, Size size) {
    final linePaint = Paint()
      ..color = Colors.green // Line color when connected
      ..strokeWidth = 4.0
      ..strokeCap = StrokeCap.round;

    final pointPaint = Paint()
      ..strokeWidth = 10.0 // Make points larger
      ..strokeCap = StrokeCap.round;

    // Draw points
    for (int i = 0; i < points.length; i++) {
      pointPaint.color = connectedOriginalIndices.contains(i) ? Colors.green : Colors.red;
      canvas.drawPoints(PointMode.points, [points[i]], pointPaint);
    }

    // Draw lines between connected points based on the order in connectedOriginalIndices
    if (connectedOriginalIndices.length > 1) {
      for (int i = 0; i < connectedOriginalIndices.length - 1; i++) {
        // Get the actual points from the  list using their original indices
        Offset p1 = points[connectedOriginalIndices[i]];
        Offset p2 = points[connectedOriginalIndices[i+1]];
        canvas.drawLine(p1, p2, linePaint);
      }
    }

    // If completed and it's a shape that should be closed (more than 2 points)
    if (isCompleted && points.length > 2) {
        // Draw a line from the last point in sequence back to the first point in sequence
        Offset lastPoint = points[connectedOriginalIndices.last];
        Offset firstPoint = points[connectedOriginalIndices.first];
        canvas.drawLine(lastPoint, firstPoint, linePaint);
    }
  }

  @override
  bool shouldRepaint(covariant _ConnectTheDotsPainter oldDelegate) {
    return oldDelegate.connectedOriginalIndices != connectedOriginalIndices || oldDelegate.isCompleted != isCompleted;
  }
}
