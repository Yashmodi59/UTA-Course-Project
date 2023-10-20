
package bufmgr;

import diskmgr.*;
import global.*;

  /**
   * class Policy is a subclass of class Replacer use the given replacement
   * policy algorithm for page replacement
   */
class LRU extends Replacer {   
//replace Policy above with impemented policy name (e.g., Lru, Clock)

  //
  // Frame State Constants
  //
  protected static final int AVAILABLE = 10;
  protected static final int REFERENCED = 11;
  protected static final int PINNED = 12;

  //Following are the fields required for LRU and MRU policies:
  /**
   * private field
   * An array to hold number of frames in the buffer pool
   */

    private int  frames[];
 
  /**
   * private field
   * number of frames used
   */   
  private int  nframes;

  /** Clock head; required for the default clock algorithm. */
  protected int head;

  /**
   * This pushes the given frame to the end of the list.
   * @param frameNo	the frame number
   */
  private void update(int frameNo)
  {
    /*
     * Move all the frames in the queue one place to the right to fill the space of the victim page
     * place it at end of the queue
     */
    int index;
    for ( index=0; index < nframes; ++index )
       if ( frames[index] == frameNo )
           break;
    // System.out.print(index);
    index ++;  // Here I able to know difference between i++ and ++i;
    for (int i = index; i<nframes; ++i){
      frames[i-1] = frames[i];
    }
    //  System.out.println(index);
       frames[nframes-1] = frameNo;

    // int index;
    // for ( index=0; index < nframes; ++index )
    //    if ( frames[index] == frameNo )
    //        break;
    // System.out.println(index);
    // /* Move all the index to one position instead of first one */
    // for (int i = 0; i < frames.length -1; i++) {
    //   frames[i] = frames[i+1];
    // }
    // /*Last and second last index will be same */
    // frames[frames.length-1] = frameNo; //replace the last with victim frame
     //This function is to be used for LRU and MRU
  }
  /**
   * Class constructor
   * Initializing frames[] pinter = null.
   */
    public LRU(BufMgr mgrArg)
    {
      super(mgrArg);
      // initialize the frame states
    for (int i = 0; i < frametab.length; i++) {
      frametab[i].state = AVAILABLE;
    }
      // initialize parameters for LRU and MRU
      nframes = 0;
      frames = new int[frametab.length];

    // initialize the clock head for Clock policy
    head = -1;
    // name();
    }
  /**
   * Notifies the replacer of a new page.
   */
  public void newPage(FrameDesc fdesc) {
    // no need to update frame state
  }

  /**
   * Notifies the replacer of a free page.
   */
  public void freePage(FrameDesc fdesc) {
    fdesc.state = AVAILABLE;
  }

  /**
   * Notifies the replacer of a pined page.
   */
  public void pinPage(FrameDesc fdesc) {
        
  }

  /**
   * Notifies the replacer of an unpinned page.
   */
  public void unpinPage(FrameDesc fdesc) {

  }
  
  /**
   * Finding a free frame in the buffer pool
   * or choosing a page to replace using your policy
   *
   * @return 	return the frame number
   *		return -1 if failed
   */

 public int pickVictim()
 {
    int frameIndex; // Initialize the frames
   //remove the below statement and write your code
	  //  return 1; //for compilation
    if(nframes< frametab.length){
      /* Fill  the frames until it not exceed the frametab length

       *we add the page to the end of the buffer pool
       *by returning the corresponding free frame
       */
      frameIndex = nframes;
      nframes++;
      // System.out.println("nframes - " + nframes++);
      // nframes = nframes+1;
      frames[frameIndex] = frameIndex; // Store at the end of frame

      // System.out.println(frameNumber+":"+frametab[frameNumber].state);
      frametab[frameIndex].state = PINNED; // Make last index pinned
      // nframes++;
      return frameIndex; 
    }
    // else{
      /*
       * if the buffer is full get thr first unpin page which is least recently used.
       */

      for (int i = 0; i < frames.length; i++) {//Iterate the frame to check the unpinned page
      frameIndex = frames[i];
      if(frametab[frameIndex].state != PINNED){
        frametab[frameIndex].state = PINNED;
        update(frameIndex);// call update function to replace the Least Recent Used frame
        return frameIndex; // return the first encountered pinned frame
      }
    }
    // }
    /*If the buffer is full and checked for the pin page than return -1 */
    return -1;
  
 }
 }

