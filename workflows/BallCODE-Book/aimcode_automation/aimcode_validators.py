"""
AIMCODE Validators
Automated validation against AIMCODE's five pillars
"""

import re
from typing import Dict, List, Any


class ZhangValidator:
    """Validates Zhang (Story Framework) principles"""
    
    BASKETBALL_TERMS = [
        "basketball", "court", "ball", "game", "player", "defense", 
        "offense", "dribble", "shoot", "pass", "rebound", "foul",
        "free throw", "three pointer", "layup", "jump shot"
    ]
    
    EXPLANATION_PHRASES = [
        "today we're learning",
        "let's learn about",
        "this concept is",
        "we will learn",
        "in this lesson",
        "today's lesson"
    ]
    
    def validate(self, content: str) -> Dict[str, Any]:
        """Validate content against Zhang principles"""
        content_lower = content.lower()
        
        checks = {
            "starts_with_basketball": self._check_starts_with_basketball(content),
            "basketball_context_clear": self._check_basketball_context(content_lower),
            "concept_emerges_naturally": self._check_concept_emerges(content),
            "no_explanation_first": self._check_no_explanation_first(content),
            "basketball_success_demonstrates_learning": self._check_success_demonstrates_learning(content_lower)
        }
        
        passed = all(checks.values())
        
        return {
            "pillar": "Zhang (Story Framework)",
            "passed": passed,
            "checks": checks,
            "score": sum(checks.values()) / len(checks),
            "feedback": self._generate_feedback(checks)
        }
    
    def _check_starts_with_basketball(self, content: str) -> bool:
        """Check if content starts with basketball action"""
        first_200 = content[:200].lower()
        return any(term in first_200 for term in self.BASKETBALL_TERMS)
    
    def _check_basketball_context(self, content: str) -> bool:
        """Check if basketball context is clear throughout"""
        basketball_count = sum(1 for term in self.BASKETBALL_TERMS if term in content)
        return basketball_count >= 5  # At least 5 basketball terms
    
    def _check_concept_emerges(self, content: str) -> bool:
        """Check if coding concept emerges naturally from basketball"""
        # Look for pattern: basketball situation → problem → concept
        has_basketball_situation = any(term in content[:500].lower() for term in self.BASKETBALL_TERMS)
        has_problem = any(word in content.lower() for word in ["problem", "challenge", "struggle", "difficulty"])
        has_concept = any(word in content.lower() for word in ["code", "program", "algorithm", "function", "loop", "if", "then"])
        
        # Concept should appear after basketball situation
        basketball_pos = min([content.lower().find(term) for term in self.BASKETBALL_TERMS if term in content.lower()] or [9999])
        concept_pos = min([content.lower().find(word) for word in ["code", "program", "algorithm"] if word in content.lower()] or [9999])
        
        return has_basketball_situation and has_problem and (concept_pos > basketball_pos)
    
    def _check_no_explanation_first(self, content: str) -> bool:
        """Check that concepts aren't explained before showing in context"""
        first_500 = content[:500].lower()
        return not any(phrase in first_500 for phrase in self.EXPLANATION_PHRASES)
    
    def _check_success_demonstrates_learning(self, content: str) -> bool:
        """Check if basketball success demonstrates learning"""
        success_words = ["success", "win", "victory", "succeed", "master", "complete"]
        learning_words = ["learn", "understand", "master", "grasp", "comprehend"]
        
        has_success = any(word in content for word in success_words)
        has_learning = any(word in content for word in learning_words)
        
        return has_success and has_learning
    
    def _generate_feedback(self, checks: Dict[str, bool]) -> List[str]:
        """Generate feedback based on validation results"""
        feedback = []
        
        if not checks["starts_with_basketball"]:
            feedback.append("❌ Story should start with basketball action, not concept explanation")
        
        if not checks["basketball_context_clear"]:
            feedback.append("❌ Basketball context should be clear throughout the story")
        
        if not checks["concept_emerges_naturally"]:
            feedback.append("❌ Coding concept should emerge from basketball situation, not be explained first")
        
        if not checks["no_explanation_first"]:
            feedback.append("❌ Don't start with 'Today we're learning about...' - start with basketball action")
        
        if not checks["basketball_success_demonstrates_learning"]:
            feedback.append("❌ Basketball success should demonstrate learning mastery")
        
        if all(checks.values()):
            feedback.append("✅ All Zhang (Story Framework) principles met!")
        
        return feedback


class ResnickValidator:
    """Validates Resnick (Constructionist/Building Activities) principles"""
    
    BUILDING_KEYWORDS = [
        "build", "create", "make", "construct", "drag", "block", 
        "code", "program", "write", "design", "assemble"
    ]
    
    BLOCK_CODING_KEYWORDS = [
        "block", "drag", "drop", "snap", "sequence", "block coding"
    ]
    
    def validate(self, content: str) -> Dict[str, Any]:
        """Validate content against Resnick principles"""
        content_lower = content.lower()
        
        checks = {
            "building_activity_included": self._check_building_activity(content_lower),
            "block_coding_mentioned": self._check_block_coding(content_lower),
            "hands_on_activity_clear": self._check_hands_on_activity(content_lower),
            "students_create_not_consume": self._check_creation_focus(content_lower)
        }
        
        passed = all(checks.values())
        
        return {
            "pillar": "Resnick (Building Activities)",
            "passed": passed,
            "checks": checks,
            "score": sum(checks.values()) / len(checks),
            "feedback": self._generate_feedback(checks)
        }
    
    def _check_building_activity(self, content: str) -> bool:
        """Check if building activity is included"""
        return any(keyword in content for keyword in self.BUILDING_KEYWORDS)
    
    def _check_block_coding(self, content: str) -> bool:
        """Check if block coding is mentioned"""
        return any(keyword in content for keyword in self.BLOCK_CODING_KEYWORDS)
    
    def _check_hands_on_activity(self, content: str) -> bool:
        """Check if hands-on activity is clear"""
        hands_on_phrases = [
            "try it yourself", "build it", "create it", "hands on",
            "practice", "exercise", "challenge", "activity"
        ]
        return any(phrase in content for phrase in hands_on_phrases)
    
    def _check_creation_focus(self, content: str) -> bool:
        """Check if focus is on creation, not consumption"""
        creation_words = ["create", "build", "make", "design", "write", "code"]
        consumption_words = ["read", "watch", "listen", "observe"]
        
        creation_count = sum(1 for word in creation_words if word in content)
        consumption_count = sum(1 for word in consumption_words if word in content)
        
        return creation_count >= consumption_count
    
    def _generate_feedback(self, checks: Dict[str, bool]) -> List[str]:
        """Generate feedback based on validation results"""
        feedback = []
        
        if not checks["building_activity_included"]:
            feedback.append("❌ Include hands-on building activities")
        
        if not checks["block_coding_mentioned"]:
            feedback.append("❌ Mention block coding exercises")
        
        if not checks["hands_on_activity_clear"]:
            feedback.append("❌ Make hands-on activities clear and accessible")
        
        if not checks["students_create_not_consume"]:
            feedback.append("❌ Focus on students creating, not just consuming content")
        
        if all(checks.values()):
            feedback.append("✅ All Resnick (Building Activities) principles met!")
        
        return feedback


class ReggioValidator:
    """Validates Reggio (Multiple Entry Points) principles"""
    
    MODE_KEYWORDS = [
        "story mode", "game mode", "code mode", "visual mode",
        "multiple ways", "different paths", "choose your path"
    ]
    
    CHOICE_KEYWORDS = [
        "choose", "select", "decide", "option", "path", "way", "mode"
    ]
    
    def validate(self, content: str) -> Dict[str, Any]:
        """Validate content against Reggio principles"""
        content_lower = content.lower()
        
        checks = {
            "multiple_modes_mentioned": self._check_multiple_modes(content_lower),
            "student_choice_emphasized": self._check_student_choice(content_lower),
            "visual_elements_included": self._check_visual_elements(content_lower)
        }
        
        passed = all(checks.values())
        
        return {
            "pillar": "Reggio (Multiple Entry Points)",
            "passed": passed,
            "checks": checks,
            "score": sum(checks.values()) / len(checks),
            "feedback": self._generate_feedback(checks)
        }
    
    def _check_multiple_modes(self, content: str) -> bool:
        """Check if multiple modes are mentioned"""
        return any(keyword in content for keyword in self.MODE_KEYWORDS)
    
    def _check_student_choice(self, content: str) -> bool:
        """Check if student choice is emphasized"""
        return any(keyword in content for keyword in self.CHOICE_KEYWORDS)
    
    def _check_visual_elements(self, content: str) -> bool:
        """Check if visual elements are included"""
        visual_keywords = ["diagram", "visual", "illustration", "image", "picture", "chart", "map"]
        return any(keyword in content for keyword in visual_keywords)
    
    def _generate_feedback(self, checks: Dict[str, bool]) -> List[str]:
        """Generate feedback based on validation results"""
        feedback = []
        
        if not checks["multiple_modes_mentioned"]:
            feedback.append("❌ Mention multiple entry points (story, game, code, visual modes)")
        
        if not checks["student_choice_emphasized"]:
            feedback.append("❌ Emphasize student choice in how they engage")
        
        if not checks["visual_elements_included"]:
            feedback.append("❌ Include visual elements (diagrams, illustrations)")
        
        if all(checks.values()):
            feedback.append("✅ All Reggio (Multiple Entry Points) principles met!")
        
        return feedback


class HassabisValidator:
    """Validates Hassabis (Systematic Progression) principles"""
    
    def validate(self, content: str, episode_number: int = None) -> Dict[str, Any]:
        """Validate content against Hassabis principles"""
        content_lower = content.lower()
        
        checks = {
            "builds_on_previous": self._check_builds_on_previous(content_lower, episode_number),
            "concept_connections_clear": self._check_concept_connections(content_lower),
            "deep_understanding_emphasized": self._check_deep_understanding(content_lower)
        }
        
        passed = all(checks.values())
        
        return {
            "pillar": "Hassabis (Systematic Progression)",
            "passed": passed,
            "checks": checks,
            "score": sum(checks.values()) / len(checks),
            "feedback": self._generate_feedback(checks, episode_number)
        }
    
    def _check_builds_on_previous(self, content: str, episode_number: int) -> bool:
        """Check if content builds on previous episodes"""
        if episode_number is None or episode_number == 1:
            return True  # First episode doesn't need to build on previous
        
        build_keywords = ["builds on", "previous", "earlier", "before", "foundation"]
        return any(keyword in content for keyword in build_keywords)
    
    def _check_concept_connections(self, content: str) -> bool:
        """Check if concept connections are clear"""
        connection_keywords = ["connect", "link", "relate", "system", "together", "integrate"]
        return any(keyword in content for keyword in connection_keywords)
    
    def _check_deep_understanding(self, content: str) -> bool:
        """Check if deep understanding is emphasized"""
        understanding_keywords = ["understand", "comprehend", "grasp", "master", "deep", "thorough"]
        return any(keyword in content for keyword in understanding_keywords)
    
    def _generate_feedback(self, checks: Dict[str, bool], episode_number: int) -> List[str]:
        """Generate feedback based on validation results"""
        feedback = []
        
        if not checks["builds_on_previous"] and episode_number > 1:
            feedback.append(f"❌ Episode {episode_number} should build on previous episodes")
        
        if not checks["concept_connections_clear"]:
            feedback.append("❌ Make concept connections to larger systems clear")
        
        if not checks["deep_understanding_emphasized"]:
            feedback.append("❌ Emphasize deep understanding over surface knowledge")
        
        if all(checks.values()):
            feedback.append("✅ All Hassabis (Systematic Progression) principles met!")
        
        return feedback


class JobsValidator:
    """Validates Jobs (Simple, Beautiful Design) principles"""
    
    def validate(self, content: str) -> Dict[str, Any]:
        """Validate content against Jobs principles"""
        content_lower = content.lower()
        
        checks = {
            "simple_structure": self._check_simple_structure(content),
            "intuitive_navigation": self._check_intuitive_navigation(content_lower),
            "beautiful_presentation": self._check_beautiful_presentation(content_lower)
        }
        
        passed = all(checks.values())
        
        return {
            "pillar": "Jobs (Simple Design)",
            "passed": passed,
            "checks": checks,
            "score": sum(checks.values()) / len(checks),
            "feedback": self._generate_feedback(checks)
        }
    
    def _check_simple_structure(self, content: str) -> bool:
        """Check if structure is simple and clear"""
        # Check for clear headings and organization
        heading_count = content.count("#")
        paragraph_count = len([p for p in content.split("\n\n") if p.strip()])
        
        # Good structure has headings and organized paragraphs
        return heading_count >= 3 and paragraph_count >= 5
    
    def _check_intuitive_navigation(self, content: str) -> bool:
        """Check if navigation is intuitive"""
        nav_keywords = ["next", "previous", "continue", "back", "forward", "step"]
        return any(keyword in content for keyword in nav_keywords)
    
    def _check_beautiful_presentation(self, content: str) -> bool:
        """Check if presentation is beautiful and engaging"""
        engaging_keywords = ["beautiful", "engaging", "inspiring", "clear", "simple", "elegant"]
        return any(keyword in content for keyword in engaging_keywords)
    
    def _generate_feedback(self, checks: Dict[str, bool]) -> List[str]:
        """Generate feedback based on validation results"""
        feedback = []
        
        if not checks["simple_structure"]:
            feedback.append("❌ Ensure simple, clear structure")
        
        if not checks["intuitive_navigation"]:
            feedback.append("❌ Make navigation intuitive and clear")
        
        if not checks["beautiful_presentation"]:
            feedback.append("❌ Ensure beautiful, engaging presentation")
        
        if all(checks.values()):
            feedback.append("✅ All Jobs (Simple Design) principles met!")
        
        return feedback


class AIMCODEValidator:
    """Complete AIMCODE validation system"""
    
    def __init__(self):
        self.zhang = ZhangValidator()
        self.resnick = ResnickValidator()
        self.reggio = ReggioValidator()
        self.hassabis = HassabisValidator()
        self.jobs = JobsValidator()
    
    def validate_all(self, content: str, episode_number: int = None) -> Dict[str, Any]:
        """Validate content against all AIMCODE pillars"""
        results = {
            "zhang": self.zhang.validate(content),
            "resnick": self.resnick.validate(content),
            "reggio": self.reggio.validate(content),
            "hassabis": self.hassabis.validate(content, episode_number),
            "jobs": self.jobs.validate(content)
        }
        
        all_passed = all([r["passed"] for r in results.values()])
        overall_score = sum([r["score"] for r in results.values()]) / len(results)
        
        return {
            "passed": all_passed,
            "overall_score": overall_score,
            "results": results,
            "summary": self._generate_summary(results, all_passed)
        }
    
    def _generate_summary(self, results: Dict[str, Any], all_passed: bool) -> str:
        """Generate summary of validation results"""
        if all_passed:
            return "✅ All AIMCODE principles met! Content is ready."
        
        failed_pillars = [name for name, result in results.items() if not result["passed"]]
        return f"⚠️ Some AIMCODE principles need attention: {', '.join(failed_pillars)}"



