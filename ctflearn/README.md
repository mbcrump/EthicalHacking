

```

    class Program
    {
        public static int finalAnswer = 0;
        public static int finalAnswer2 = 0;
        static void Main(string[] args)
        {

            string text = System.IO.File.ReadAllText(@"data.dat");
            // Display the file contents to the console. Variable text is a string.
            //System.Console.WriteLine("Contents of WriteText.txt = {0}", text);
            string[] lines = System.IO.File.ReadAllLines(@"data.dat");

            foreach (string line in lines)
            {
                var answer = Regex.Matches(line, "0").Count;
                var answer2 = Regex.Matches(line, "1").Count;

                if (answer % 3 == 0 || answer2 % 2 == 0)
                {
                    finalAnswer++;
                }

              


            }

            var answernew = finalAnswer + finalAnswer2;
            Console.WriteLine(answernew.ToString());
        }
    }

```
