import 'package:firebase_auth/firebase_auth.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class AuthService {
  final FirebaseAuth _auth = FirebaseAuth.instance;
  final FirebaseFirestore _firestore = FirebaseFirestore.instance;

  // Get current user
  User? get currentUser => _auth.currentUser;

  // Sign in with email and password
  Future<UserCredential?> signInWithEmailAndPassword(String email, String password) async {
    try {
      return await _auth.signInWithEmailAndPassword(email: email, password: password);
    } on FirebaseAuthException catch (e) {
      // Handle specific errors if needed, e.g., user-not-found, wrong-password
      print('Error signing in: ${e.message}');
      return null;
    }
  }

  // Register with email and password
  Future<UserCredential?> registerWithEmailAndPassword(String email, String password) async {
    try {
      return await _auth.createUserWithEmailAndPassword(email: email, password: password);
    } on FirebaseAuthException catch (e) {
      // Handle specific errors, e.g., email-already-in-use, weak-password
      print('Error registering: ${e.message}');
      return null;
    }
  }

  // Sign out
  Future<void> signOut() async {
    await _auth.signOut();
  }

  // Create child profile (MVP: name only, single child per parent)
  Future<void> createChildProfile(String parentUid, String childName) async {
    try {
      // For MVP, we can store the child's name directly in the parent's document
      // or in a subcollection. For simplicity, let's add it to the parent's doc.
      // A more robust solution might use a 'children' subcollection.
      await _firestore.collection('users').doc(parentUid).set({
        'childName': childName,
        // Avatar stub can be a placeholder string or default image path
        'childAvatarStub': 'default_avatar.png'
      }, SetOptions(merge: true)); // merge:true to not overwrite other parent data
    } catch (e) {
      print('Error creating child profile: $e');
      // Handle error appropriately
    }
  }

  // Get child profile (MVP)
  Future<Map<String, dynamic>?> getChildProfile(String parentUid) async {
    try {
      DocumentSnapshot doc = await _firestore.collection('users').doc(parentUid).get();
      if (doc.exists && doc.data() != null) {
        // Assuming childName and childAvatarStub are stored directly
        var data = doc.data() as Map<String, dynamic>;
        if (data.containsKey('childName')) {
          return {'childName': data['childName'], 'childAvatarStub': data['childAvatarStub']};
        }
      }
      return null;
    } catch (e) {
      print('Error fetching child profile: $e');
      return null;
    }
  }
}
