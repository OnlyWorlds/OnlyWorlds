using System;
using System.Collections.Generic;
[System.Serializable]
public class Trait : BaseElement
{
    // Qualitative
    public string SocialEffects;
    public string PhysicalEffects;
    public string FunctionalEffects;
    public string PersonalityEffects;
    public string BehaviourEffects;
    // Quantitative
    public int? Charisma;
    public int? Coercion;
    public int? Competence;
    public int? Compassion;
    public int? Creativity;
    public int? Courage;
    // World
    public string Significance;
    public string AntiTraitId;
    public List<string> EmpoweredAbilitiesIds; = new List<string>();
}
