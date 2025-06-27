using System;
using System.Collections.Generic;
[System.Serializable]
public class Language : BaseElement
{
    // Structure
    public string Phonology;
    public string Grammar;
    public string Lexicon;
    public string Writing;
    public string ClassificationId;
    // World
    public string Status;
    public List<string> SpreadIds; = new List<string>();
    public List<string> DialectsIds; = new List<string>();
}
