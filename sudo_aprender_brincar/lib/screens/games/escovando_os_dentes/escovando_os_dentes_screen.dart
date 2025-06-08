import 'package:flutter/material.dart';

class EscovandoOsDentesScreen extends StatefulWidget {
  const EscovandoOsDentesScreen({super.key});

  @override
  State<EscovandoOsDentesScreen> createState() => _EscovandoOsDentesScreenState();
}

class _EscovandoOsDentesScreenState extends State<EscovandoOsDentesScreen> {
  int _currentStep = 0; // 0: Apply Paste, 1: Brush Teeth, 2: Rinse, 3: Finished

  // Placeholder images - in a real app, these would be in assets/
  final String _toothbrushImage = 'assets/images/toothbrush.png'; // Placeholder path
  final String _toothpasteImage = 'assets/images/toothpaste.png'; // Placeholder path
  final String _teethImage = 'assets/images/teeth_normal.png'; // Placeholder path
  final String _teethBrushedImage = 'assets/images/teeth_brushed.png'; // Placeholder path
  final String _cupImage = 'assets/images/cup.png'; // Placeholder path
  final String _avatarHappyImage = 'assets/images/avatar_happy.png'; // Placeholder path

  // For MVP, we'll simulate asset loading.
  // In a real app, ensure these assets exist and are listed in pubspec.yaml
  // For now, we'll use colored containers as placeholders if images are not truly available.

  Widget _buildStepWidget() {
    switch (_currentStep) {
      case 0: // Apply Paste
        return Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text('Passo 1: Coloque a pasta na escova', style: TextStyle(fontSize: 20)),
            const SizedBox(height: 20),
            // Simulate draggable items or tap interaction
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                // Draggable<String>(
                //   data: 'toothpaste',
                //   feedback: _placeholderAssetWidget(_toothpasteImage, 'Pasta', Colors.blue, 50),
                //   childWhenDragging: Container(),
                //   child: _placeholderAssetWidget(_toothpasteImage, 'Pasta', Colors.blue, 100),
                // ),
                // DragTarget<String>(
                //   builder: (context, candidateData, rejectedData) {
                //     return _placeholderAssetWidget(_toothbrushImage, 'Escova', Colors.grey, 100);
                //   },
                //   onAccept: (data) {
                //     if (data == 'toothpaste') {
                //       setState(() => _currentStep = 1);
                //     }
                //   },
                // ),
                _placeholderAssetWidget(_toothpasteImage, 'Pasta', Colors.blue, 100),
                _placeholderAssetWidget(_toothbrushImage, 'Escova', Colors.grey, 100),
              ],
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () => setState(() => _currentStep = 1),
              child: const Text('Simular aplicar pasta'),
            ),
          ],
        );
      case 1: // Brush Teeth
        return Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text('Passo 2: Escove os dentes', style: TextStyle(fontSize: 20)),
            const SizedBox(height: 20),
            _placeholderAssetWidget(_teethImage, 'Dentes', Colors.redAccent, 150),
            const SizedBox(height: 10),
            const Text('Clique nos dentes para escovar (simulado)'),
             // In a real game, this would be interactive (dragging brush over teeth)
            ElevatedButton(
              onPressed: () => setState(() => _currentStep = 2),
              child: const Text('Simular escovar'),
            ),
          ],
        );
      case 2: // Rinse
        return Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text('Passo 3: Enxágue a boca', style: TextStyle(fontSize: 20)),
            const SizedBox(height: 20),
            _placeholderAssetWidget(_cupImage, 'Copo com Água', Colors.lightBlue, 100),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () => setState(() => _currentStep = 3),
              child: const Text('Simular enxaguar'),
            ),
          ],
        );
      case 3: // Finished
        return Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text('Muito bem! Dentes limpinhos!', style: TextStyle(fontSize: 24, color: Colors.green)),
            const SizedBox(height: 20),
            _placeholderAssetWidget(_avatarHappyImage, 'Avatar Feliz', Colors.orange, 150),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                // Navigate back to Lobby or show score
                if (Navigator.canPop(context)) Navigator.pop(context);
              },
              child: const Text('Voltar ao Lobby'),
            ),
          ],
        );
      default:
        return const Center(child: Text('Erro no jogo!'));
    }
  }

  Widget _placeholderAssetWidget(String assetPath, String altText, Color color, double size) {
    // In MVP, we use a colored container as a placeholder for actual images.
    // In a real app, you'd use Image.asset(assetPath) after adding images to assets folder
    // and declaring them in pubspec.yaml.
    return Container(
      width: size,
      height: size,
      color: color,
      alignment: Alignment.center,
      child: Text(altText, style: const TextStyle(color: Colors.white), textAlign: TextAlign.center,),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Jogo: Escovando os Dentes (MVP)'),
        leading: IconButton(
          icon: const Icon(Icons.close),
          onPressed: () {
             if (Navigator.canPop(context)) Navigator.pop(context);
          },
        ),
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: _buildStepWidget(),
        ),
      ),
    );
  }
}
