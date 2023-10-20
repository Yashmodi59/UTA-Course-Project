import java.io.IOException;
import java.util.StringTokenizer;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.input.FileSplit;
import org.apache.hadoop.mapreduce.lib.input.MultipleInputs;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;

public class MapReduceProgram{
    public static class TokenizerMapper1
    extends Mapper < Object, Text, Text, Text > {
        private Text word = new Text();
        private Text re = new Text();
        public void map(Object key, Text value, Context context) throws IOException,
        InterruptedException {
            FileSplit fileSplit = (FileSplit) context.getInputSplit();
            String filename = fileSplit.getPath().getName();
            String line = value.toString();
            String tokens[] = line.split("\t");
            if (tokens.length == 9){
                int n = tokens.length;
                String mapperKey = tokens[0];
                String type = tokens[1];
                String primaryTitle = tokens[2];
                String year = tokens[5];
                if(!year.equals("\\n") && type == "tvMovie" && Integer.parseInt(year) >= 1977 && Integer.parseInt(year) <= 1987){
                    word.set(mapperKey);
                    re.set("type_"+type + "_" + "year_"+year + "primaryTitle_" + primaryTitle);
                    context.write(word,re);
                }
            }
        }
    }

    public static class TokenizerMapper2
    extends Mapper < Object, Text, Text, Text > {
        private Text word = new Text();
        private Text re = new Text();
        public void map(Object key, Text value, Context context) throws IOException,
        InterruptedException {
            FileSplit fileSplit = (FileSplit) context.getInputSplit();
            String filename = fileSplit.getPath().getName();
            String line = value.toString();
            String tokens[] = line.split(",");
            if (tokens.length == 3){
                int n = tokens.length;
                String mapperKey = tokens[0];
                String actorId = tokens[1];
                String actorName = tokens[2];
                    word.set(mapperKey);
                    re.set("actorId_"+actorId + "_actorName_" + actorName);
                    context.write(word,re);
            }
        }
    }
    public static class TokenizerMapper3
    extends Mapper < Object, Text, Text, Text > {
        private Text word = new Text();
        private Text re = new Text();
        public void map(Object key, Text value, Context context) throws IOException,
        InterruptedException {
            FileSplit fileSplit = (FileSplit) context.getInputSplit();
            String filename = fileSplit.getPath().getName();
            String line = value.toString();
            String tokens[] = line.split("\t");
            if (tokens.length == 3){
                int n = tokens.length;
                String mapperKey = tokens[0];
                String directorId = tokens[1];
                word.set(mapperKey);
                re.set("directorId_"+directorId);
                context.write(word,re);
            }
        }
    }
    public static class IntSumReducer
    extends Reducer < Text, Text, Text, Text > {
        private Text  result = new Text();
        public void reduce(Text key, Iterable < Text > values, Context context) throws IOException,
        InterruptedException {
            String s = "";
            for (Text t: values){
                s += "_" + t;
            }
            result.set(s);
            context.write(key,result);
        }
    }
    public static void main(String[] args){
        Configuration conf = new Configuration();
        int split = 700*1024*1024; // This is in bytes
        String splitsize = Integer.toString(split);
        conf.set("mapreduce.input.fileinputformat.split.minsize",splitsize);
        // conf.set("mapreduce.map.memory.mb", "2048"); // This is in Mb
        // conf.set("mapreduce.reduce.memory.mb", "2048"); 
        try{
        Job job =  Job.getInstance(conf, "word count");
        job.setJarByClass(MapReduceProgram.class);
        MultipleInputs.addInputPath(job,new Path(args[0]), TextInputFormat.class, TokenizerMapper1.class);
        MultipleInputs.addInputPath(job,new Path(args[1]), TextInputFormat.class, TokenizerMapper2.class);
        MultipleInputs.addInputPath(job,new Path(args[2]), TextInputFormat.class, TokenizerMapper3.class);
        job.setReducerClass(IntSumReducer.class);
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(Text.class);
        job.setOutputValueClass(Text.class);
        job.setOutputKeyClass(Text.class);
        FileOutputFormat.setOutputPath(job, new Path(args[3]+"inter"));
        try {
            job.waitForCompletion(true);
        } catch (Exception e) {
            // TODO: handle exception
        }
        }
        catch(IOException exception){
            
        }
        System.exit(0);
    }
}