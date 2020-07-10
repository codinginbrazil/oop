#import <Foundation/Foundation.h>

int main(void){
    NSAutoreleasePool* pool = [[NSAutoreleasePool alloc] init];
    
    NSString *s = @"Hello World";
    [[NSFileHandle fileHandleWithStandardOutput] writeData: [s dataUsingEncoding: NSUTF8StringEncoding]];
    [pool release];
    return 0;
}