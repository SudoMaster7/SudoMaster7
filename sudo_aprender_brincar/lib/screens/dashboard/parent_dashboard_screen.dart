import 'package:flutter/material.dart';
import 'package:sudo_aprender_brincar/services/auth_service.dart'; // For user info if needed

class ParentDashboardScreen extends StatefulWidget {
  const ParentDashboardScreen({super.key});

  @override
  State<ParentDashboardScreen> createState() => _ParentDashboardScreenState();
}

class _ParentDashboardScreenState extends State<ParentDashboardScreen> {
  final AuthService _authService = AuthService();
  String? _parentEmail;
  String? _childName; // Added to display child's name

  // MVP: Placeholder data for progress
  final List<Map<String, String>> _gamesPlayed = [
    {'name': 'Escovando os Dentes', 'status': 'Completado 2 vezes'},
    {'name': 'Conecte os Pontos', 'status': 'Jogou 3 vezes'},
    {'name': 'Respiração da Flor', 'status': 'Usado 1 vez'},
  ];
  final String _totalTimeSpent = "15 minutos (MVP)"; // Placeholder

  @override
  void initState() {
    super.initState();
    _loadUserData();
  }

  Future<void> _loadUserData() async {
    final user = _authService.currentUser;
    if (user != null) {
      final profile = await _authService.getChildProfile(user.uid);
      if(mounted){
        setState(() {
          _parentEmail = user.email;
          if (profile != null) {
            _childName = profile['childName'];
          } else {
            _childName = "Criança";
          }
        });
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Painel de Progresso (${_childName ?? "Criança"})'),
      ),
      body: ListView(
        padding: const EdgeInsets.all(16.0),
        children: <Widget>[
          Text(
            'Email do Responsável: ${_parentEmail ?? "N/A"}',
            style: const TextStyle(fontSize: 16, fontStyle: FontStyle.italic),
          ),
          const SizedBox(height: 20),
          Card(
            elevation: 2,
            child: ListTile(
              title: const Text('Tempo Total no App (MVP)'),
              subtitle: Text(_totalTimeSpent),
              leading: const Icon(Icons.timer_outlined, color: Colors.blueAccent),
            ),
          ),
          const SizedBox(height: 20),
          const Text(
            'Atividade nos Jogos (Dados Fictícios - MVP):',
            style: TextStyle(fontSize: 16, fontWeight: FontWeight.w600),
          ),
          const Divider(thickness:1),
          ..._gamesPlayed.map((game) {
            return Card(
              elevation: 2,
              margin: const EdgeInsets.symmetric(vertical: 6),
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
              child: ListTile(
                leading: Icon(Icons.gamepad_outlined, color: Theme.of(context).primaryColor),
                title: Text(game['name']!, style: const TextStyle(fontWeight: FontWeight.bold)),
                subtitle: Text(game['status']!),
                trailing: const Icon(Icons.arrow_forward_ios_rounded, size: 16, color: Colors.grey),
                onTap: () { /* Could navigate to detailed game stats in future */ },
              ),
            );
          }).toList(),
          const SizedBox(height: 30),
           ElevatedButton.icon(
            icon: const Icon(Icons.arrow_back),
            label: const Text('Voltar ao Lobby'),
            style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(horizontal:20, vertical:12)),
            onPressed: () {
              if (Navigator.canPop(context)) {
                Navigator.pop(context);
              }
            },
          ),
        ],
      ),
    );
  }
}
