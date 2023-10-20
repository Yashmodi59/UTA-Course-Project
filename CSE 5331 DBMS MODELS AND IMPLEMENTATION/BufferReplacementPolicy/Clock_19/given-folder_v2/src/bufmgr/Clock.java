
package bufmgr;

import diskmgr.*;
import global.*;

  /**
   * class Policy is a subclass of class Replacer use the given replacement
   * policy algorithm for page replacement
   */
class Clock extends  Replacer {   
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
   * @return 
   */
  private void update(int frameNo)
  {
     //This function is to be used for LRU and MRU
  }

  /**
   * Class constructor
   * Initializing frames[] pinter = null.
   */
    public Clock(BufMgr mgrArg)
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
  public int getState(int frameNo){
    return frametab[frameNo].state;
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
    boolean requiredFrameFound = false; // Make it true when victim frame found
    int counter = 0; // Initialised Counter to track count as it won't exceed the buufer pool length
    while (!requiredFrameFound){
      
      head = (head+1) % frametab.length; //Increment the counter to make sure that it doen't exceed the frametab size

      if (counter > 2 * frametab.length)
        return -1; // buffer frame is not free as for the first time it will exceed the pool length but maximum can 2*frametab.length
      /*
       * To give each frame 2 chance change the head state to referenced to available
       * if it already in available state than return same head pointer
       */
      if (getState(head) == REFERENCED) 
        frametab[head].state = AVAILABLE;
      
      else if (getState(head) == AVAILABLE)
        requiredFrameFound = true; // find the required frame so break the while loop

      counter++;	// increment the counter to go check for the next frame
    }
    
    return head;
  
  
    // FrameDesc frame; // initialize the fram
    // for (int i = 0; i < frametab.length; i++) { //iterate throught the lenthe
    //     frame = frametab[head];
    //     if (frame.state == AVAILABLE) {
    //         return head;
    //     }
    //     if (!(frame.state == PINNED)) {
    //         if (frame.state == REFERENCED) {
    //             frame.state = AVAILABLE;
    //         }
    //         else {
    //             return head;
    //         }
    //     }
    //     head = (++head) % frametab.length;
    // }

    //remove the below statement and write your code
 }
}