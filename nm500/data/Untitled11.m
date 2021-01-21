clear;

train4=load('train4.txt');

idx=kmedoids(train4,24);

b=zeros([24 1000]);

i=0;
h=0;
current=0;
current_y=0;
temp=0;
count=1218;

result=zeros([1218 160]);

for i=1:1218
    current=idx(i);
    current_y=1;
    while b(current,current_y)~=0
        current_y=current_y+1;
    end
    b(current,current_y)=i;
end

while count~=0
    for h=1:24
        current_y=1;
        
        while b(h,current_y)~=0
            current_y=current_y+1;
        end
        
        if current_y==1 
            temp=b(h,current_y);
        else
            temp=b(h,current_y-1);
        end
        
        if temp==0
            continue;
        end
        result(1219-count,:)=train4(temp,:);

        count=count-1;
        if count==0
            break;
        end
        
        if current_y==1
            b(h,current_y)=0;
        else
            b(h,current_y-1)=0;
        end

    end
    
end

fid=fopen('train992.txt','wt');

for i= 1:1218
	fprintf(fid,'%3d,',result(i,:));
	fprintf(fid,'\n');
end

fclose(fid);
