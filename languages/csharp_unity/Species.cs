using System;
using System.Collections.Generic;
[System.Serializable]
public class Species : BaseElement
{
    // Biology
    public string Appearance;
    public int? LifeSpan;
    public int? AverageWeight;
    public List<string> NourishmentIds; = new List<string>();
    // Psychology
    public string Instincts;
    public int? Aggression;
    public string Agency;
    public List<string> LanguagesIds; = new List<string>();
    // World
    public string Impact;
    public List<string> HabitatIds; = new List<string>();
    public List<string> InteractionIds; = new List<string>();
    public List<string> ConsumablesIds; = new List<string>();
}
