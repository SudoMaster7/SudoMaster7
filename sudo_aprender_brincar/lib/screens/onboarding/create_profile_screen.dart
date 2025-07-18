import 'package:flutter/material.dart';
import 'package:sudo_aprender_brincar/services/auth_service.dart';
import 'package:sudo_aprender_brincar/screens/lobby/lobby_screen.dart';
// Import LobbyScreen for navigation

class CreateProfileScreen extends StatefulWidget {
  final String parentUid;
  const CreateProfileScreen({super.key, required this.parentUid});

  @override
  State<CreateProfileScreen> createState() => _CreateProfileScreenState();
}

class _CreateProfileScreenState extends State<CreateProfileScreen> {
  final AuthService _authService = AuthService();
  final _formKey = GlobalKey<FormState>();
  String _childName = '';
  bool _isLoading = false;
  String _errorMessage = '';


  void _tryCreateProfile() async {
    if (_formKey.currentState!.validate()) {
      _formKey.currentState!.save();
      setState(() => _isLoading = true);
      try {
        await _authService.createChildProfile(widget.parentUid, _childName);
        // Navigate to LobbyScreen
        Navigator.of(context).pushReplacement(MaterialPageRoute(builder: (_) => const LobbyScreen()));
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text('Profile Created! (MVP: Navigate to Lobby)')),
        );
      } catch (e) {
         setState(() {
          _errorMessage = 'An error occurred: ${e.toString()}';
        });
      } finally {
        setState(() => _isLoading = false);
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Create Child Profile (MVP)')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              TextFormField(
                decoration: const InputDecoration(labelText: 'Child\'s Name'),
                validator: (value) => value!.isEmpty ? 'Please enter a name' : null,
                onSaved: (value) => _childName = value!,
              ),
              const SizedBox(height: 20),
              // Avatar stub - for MVP, just a placeholder text
              const Text('Avatar: Default (MVP)'),
              const SizedBox(height: 20),
              if (_isLoading)
                const CircularProgressIndicator()
              else
                ElevatedButton(
                  onPressed: _tryCreateProfile,
                  child: const Text('Save Profile & Start'),
                ),
               if (_errorMessage.isNotEmpty)
                Padding(
                  padding: const EdgeInsets.only(top: 10.0),
                  child: Text(
                    _errorMessage,
                    style: const TextStyle(color: Colors.red),
                    textAlign: TextAlign.center,
                  ),
                ),
            ],
          ),
        ),
      ),
    );
  }
}
