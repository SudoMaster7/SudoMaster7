import 'package:flutter/material.dart';
import 'package:sudo_aprender_brincar/services/auth_service.dart';
import 'package:sudo_aprender_brincar/screens/onboarding/login_screen.dart';
import 'package:sudo_aprender_brincar/screens/games/escovando_os_dentes/escovando_os_dentes_screen.dart';
import 'package:sudo_aprender_brincar/screens/games/conecte_os_pontos/conecte_os_pontos_screen.dart';
import 'package:sudo_aprender_brincar/screens/games/respiracao_da_flor/respiracao_da_flor_screen.dart';
import 'package:sudo_aprender_brincar/screens/dashboard/parent_dashboard_screen.dart';

class LobbyScreen extends StatefulWidget {
  const LobbyScreen({super.key});

  @override
  State<LobbyScreen> createState() => _LobbyScreenState();
}

class _LobbyScreenState extends State<LobbyScreen> {
  final AuthService _authService = AuthService();
  String? _parentEmail;
  String? _childName;
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _loadUserData();
  }

  Future<void> _loadUserData() async {
    setState(() => _isLoading = true);
    final user = _authService.currentUser;
    if (user != null) {
      _parentEmail = user.email;
      final profile = await _authService.getChildProfile(user.uid);
      if (mounted) { // Check if widget is still in the tree
        setState(() {
          if (profile != null) {
            _childName = profile['childName'];
          } else {
            _childName = "Criança"; // Default
          }
        });
      }
    }
    if (mounted) {
     setState(() => _isLoading = false);
    }
  }

  Future<void> _logout() async {
    await _authService.signOut();
    Navigator.of(context).pushAndRemoveUntil(
      MaterialPageRoute(builder: (context) => const LoginScreen()),
      (Route<dynamic> route) => false, // Remove all routes
    );
  }

  Widget _buildGameCard(BuildContext context, String title, IconData icon, VoidCallback onTap) {
    return Card(
      elevation: 4.0,
      margin: const EdgeInsets.all(10.0),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15.0)),
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(15.0),
        child: Padding(
          padding: const EdgeInsets.all(20.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Icon(icon, size: 50.0, color: Theme.of(context).primaryColor),
              const SizedBox(height: 15.0),
              Text(title, style: const TextStyle(fontSize: 18.0, fontWeight: FontWeight.bold), textAlign: TextAlign.center),
            ],
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Lobby de Jogos'),
        actions: [
          IconButton(
            icon: const Icon(Icons.logout),
            tooltip: 'Sair',
            onPressed: _logout,
          ),
        ],
      ),
      body: _isLoading
          ? const Center(child: CircularProgressIndicator())
          : RefreshIndicator(
              onRefresh: _loadUserData,
              child: ListView(
                padding: const EdgeInsets.all(10.0),
                children: <Widget>[
                  Padding(
                    padding: const EdgeInsets.symmetric(vertical: 15.0, horizontal: 8.0),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.center,
                      children: [
                        Text('Bem-vindo(a), ${_parentEmail ?? 'N/A'}!', style: const TextStyle(fontSize: 16)),
                        const SizedBox(height: 4),
                        Text('Perfil da Criança: ${_childName ?? 'Nome não definido'}', style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Colors.deepPurple)),
                      ],
                    ),
                  ),
                  const Divider(thickness: 1),
                  const Padding(
                    padding: EdgeInsets.symmetric(vertical:12.0, horizontal: 8.0),
                    child: Text("Escolha um jogo para começar:", style: TextStyle(fontSize: 18, fontWeight: FontWeight.w500)),
                  ),
                  GridView.count(
                    crossAxisCount: 2,
                    shrinkWrap: true, // Important for ListView
                    physics: const NeverScrollableScrollPhysics(), // Disable GridView's own scrolling
                    children: [
                       _buildGameCard(
                        context,
                        'Escovando os Dentes',
                        Icons.brush_rounded,
                        () => Navigator.push(context, MaterialPageRoute(builder: (_) => const EscovandoOsDentesScreen())),
                      ),
                      _buildGameCard(
                        context,
                        'Conecte os Pontos',
                        Icons.timeline_rounded,
                        () => Navigator.push(context, MaterialPageRoute(builder: (_) => const ConecteOsPontosScreen())),
                      ),
                      _buildGameCard(
                        context,
                        'Respiração da Flor',
                        Icons.self_improvement_rounded,
                        () => Navigator.push(context, MaterialPageRoute(builder: (_) => const RespiracaoDaFlorScreen())),
                      ),
                       _buildGameCard( // Placeholder for more games
                        context,
                        'Em Breve!',
                        Icons.hourglass_empty_rounded,
                        () => ScaffoldMessenger.of(context).showSnackBar(
                            const SnackBar(content: Text('Novo jogo em breve!'))),
                      ),
                    ],
                  ),
                  const SizedBox(height: 30), // Existing SizedBox
                  Center(
                    child: ElevatedButton.icon(
                      icon: const Icon(Icons.dashboard_customize_rounded),
                      label: const Text("Ver Progresso (Painel)"),
                      style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12)),
                      onPressed: () {
                        Navigator.push(context, MaterialPageRoute(builder: (_) => const ParentDashboardScreen()));
                      },
                    ),
                  ),
                  // The // DASHBOARD_BUTTON_PLACEHOLDER comment that was here is now replaced by the button above.
                ],
              ),
            ),
    );
  }
}
